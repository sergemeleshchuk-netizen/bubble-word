from __future__ import annotations

import os

import pytest

from word_content.candidate_generation import (
    expand_category,
    expand_words,
    records_to_jsonl_dicts,
    review_candidates,
)
from word_content.importers import import_membership_records
from word_content.llm.base import LLMError, call_with_retries
from word_content.llm.mock import MockLLMProvider, echo_handler
from word_content.llm.openai_compatible import OpenAICompatibleProvider, provider_from_env
from word_content.repositories import memberships_for_word
from word_content.validators import ValidationIssue

NO_SLEEP = lambda _seconds: None  # noqa: E731


def candidate(word: str, **overrides) -> dict:
    payload = {
        "word": word,
        "part_of_speech": "noun",
        "is_proper_noun": False,
        "sense_key": f"{word}_fruit",
        "sense_definition": f"The edible fruit called {word}",
        "relation_type": "is_a",
        "reason": f"{word.title()} is a common edible fruit",
        "fit_score": 0.95,
        "obviousness_score": 0.9,
        "possible_other_category_keys": ["pie_ingredients"],
        "risk_flags": [],
    }
    payload.update(overrides)
    return payload


def expansion(*words: str) -> dict:
    return {"category_key": "fruits", "candidates": [candidate(w) for w in words]}


# ------------------------------------------------------------------ category expansion


def test_valid_json_produces_records(seeded):
    provider = MockLLMProvider([expansion("pear", "plum")])
    result = expand_category(seeded, provider, category_key="fruits", count=2, batch_size=2)

    assert [r["word"] for r in result.records] == ["pear", "plum"]
    assert all(r["review_status"] == "candidate" for r in result.records)
    assert all(r["source"] == "ai_category_expansion" for r in result.records)
    assert result.hints["pear"] == ["pie_ingredients"]


def test_ai_never_marks_approved(seeded):
    provider = MockLLMProvider([expansion("pear")])
    result = expand_category(seeded, provider, category_key="fruits", count=1, batch_size=1)
    assert result.records[0]["review_status"] == "candidate"


def test_invalid_json_is_recorded_and_does_not_crash(seeded):
    provider = MockLLMProvider(["не json вовсе"])
    result = expand_category(
        seeded, provider, category_key="fruits", count=1, batch_size=1, max_retries=0
    )

    assert result.records == []
    assert result.batches_failed == 1
    row = seeded.execute("SELECT * FROM generation_runs ORDER BY id DESC LIMIT 1").fetchone()
    assert row["status"] == "error"
    assert row["raw_output_json"] == "не json вовсе"  # сырой ответ сохранён


def test_score_out_of_range_fails_validation(seeded):
    provider = MockLLMProvider([{"category_key": "fruits", "candidates": [candidate("pear", fit_score=1.4)]}])
    result = expand_category(
        seeded, provider, category_key="fruits", count=1, batch_size=1, max_retries=0
    )

    assert result.records == []
    assert result.batches_failed == 1


def test_duplicate_of_existing_membership_is_skipped(seeded):
    provider = MockLLMProvider([expansion("apple")])
    result = expand_category(seeded, provider, category_key="fruits", count=1, batch_size=1)

    assert result.records == []
    assert result.skipped[0]["reason"] == "duplicate"


def test_incomplete_sense_is_skipped(seeded):
    broken = candidate("pear")
    broken["sense_definition"] = None
    provider = MockLLMProvider([{"category_key": "fruits", "candidates": [broken]}])
    result = expand_category(seeded, provider, category_key="fruits", count=1, batch_size=1)

    assert result.records == []
    assert result.skipped[0]["reason"] == "incomplete_sense"


def test_unknown_category_key_is_rejected_before_call(seeded):
    provider = MockLLMProvider([expansion("pear")])
    with pytest.raises(ValidationIssue):
        expand_category(seeded, provider, category_key="ghost_category", count=1)


def test_partial_batch_failure_continues(seeded):
    provider = MockLLMProvider([LLMError("timeout"), expansion("plum")])
    result = expand_category(
        seeded, provider, category_key="fruits", count=4, batch_size=2, max_retries=0
    )

    assert result.batches_failed == 1
    assert result.batches_ok == 1
    assert [r["word"] for r in result.records] == ["plum"]


def test_empty_candidate_list_is_valid(seeded):
    provider = MockLLMProvider([{"category_key": "fruits", "candidates": []}])
    result = expand_category(seeded, provider, category_key="fruits", count=1, batch_size=1)

    assert result.records == []
    assert result.batches_ok == 1
    assert result.batches_failed == 0


def test_markdown_fence_is_tolerated(seeded):
    import json

    provider = MockLLMProvider(["```json\n" + json.dumps(expansion("plum")) + "\n```"])
    result = expand_category(seeded, provider, category_key="fruits", count=1, batch_size=1)
    assert [r["word"] for r in result.records] == ["plum"]


def test_generated_records_import_and_are_idempotent(seeded):
    provider = MockLLMProvider([expansion("pear", "plum")])
    result = expand_category(seeded, provider, category_key="fruits", count=2, batch_size=2)
    records = records_to_jsonl_dicts(result.records)

    first = import_membership_records(
        seeded, list(enumerate(records, 1)), source_file="test", import_type="ai"
    )
    second = import_membership_records(
        seeded, list(enumerate(records, 1)), source_file="test", import_type="ai"
    )

    assert (first.inserted, first.rejected) == (2, 0)
    assert (second.inserted, second.updated) == (0, 2)
    assert {r["review_status"] for r in memberships_for_word(seeded, "pear")} == {"candidate"}


def test_generation_run_is_recorded(seeded):
    provider = MockLLMProvider([expansion("pear")])
    result = expand_category(seeded, provider, category_key="fruits", count=1, batch_size=1)

    row = seeded.execute("SELECT * FROM generation_runs WHERE id = ?", (result.run_ids[0],)).fetchone()
    assert row["generation_type"] == "category_expansion"
    assert row["model"] == "mock-model"
    assert row["prompt_version"] == "v1"
    assert row["status"] == "ok"
    assert "pear" in row["parsed_output_json"]


# ------------------------------------------------------------------- reverse expansion


def reverse(word: str, category_key: str, **overrides) -> dict:
    membership = {
        "category_key": category_key,
        "sense_key": "apple_fruit",
        "sense_definition": "The round edible fruit of an apple tree",
        "relation_type": "used_in",
        "reason": "Apples are the classic pie filling",
        "fit_score": 0.9,
        "obviousness_score": 0.8,
        "risk_flags": [],
    }
    membership.update(overrides)
    return {"words": [{"word": word, "memberships": [membership]}]}


def test_reverse_pass_returns_new_membership(seeded):
    provider = MockLLMProvider([reverse("apple", "river_features", relation_type="part_of")])
    result = expand_words(seeded, provider, words=["apple"], batch_size=1)

    assert len(result.records) == 1
    assert result.records[0]["category_key"] == "river_features"
    assert result.records[0]["review_status"] == "candidate"


def test_reverse_pass_skips_existing_membership(seeded):
    provider = MockLLMProvider([reverse("apple", "pie_ingredients")])
    result = expand_words(seeded, provider, words=["apple"], batch_size=1)

    assert result.records == []
    assert result.skipped[0]["reason"] == "duplicate"


def test_reverse_pass_rejects_invented_category(seeded):
    provider = MockLLMProvider([reverse("apple", "healthy_things")])
    result = expand_words(seeded, provider, words=["apple"], batch_size=1)

    assert result.records == []
    assert result.skipped[0]["reason"] == "unknown_category_key"


def test_reverse_pass_accepts_empty_memberships(seeded):
    provider = MockLLMProvider([{"words": [{"word": "apple", "memberships": []}]}])
    result = expand_words(seeded, provider, words=["apple"], batch_size=1)

    assert result.records == []
    assert result.batches_ok == 1


def test_reverse_pass_batches_words(seeded):
    provider = MockLLMProvider(
        [{"words": []}, {"words": []}], model="mock-model"
    )
    expand_words(seeded, provider, words=["apple", "bank"], batch_size=1)
    assert len(provider.calls) == 2


# --------------------------------------------------------------------- критический review


def test_review_does_not_change_status(seeded):
    provider = MockLLMProvider(handler=echo_handler)
    before = {
        row["membership_id"]: row["review_status"]
        for row in memberships_for_word(seeded, "apple")
    }
    result = review_candidates(seeded, provider, statuses=["candidate"], limit=10)

    after = {
        row["membership_id"]: row["review_status"]
        for row in memberships_for_word(seeded, "apple")
    }
    assert before == after
    assert all(v["recommended_decision"] == "manual_review" for v in result.records)


def test_review_drops_unknown_membership_id(seeded):
    provider = MockLLMProvider(
        [{"verdicts": [{"membership_id": 99999, "recommended_decision": "reject"}]}]
    )
    result = review_candidates(seeded, provider, statuses=["candidate"], limit=10)

    assert result.records == []
    assert result.skipped[0]["reason"] == "unknown_membership_id"


# ------------------------------------------------------------------------- провайдеры


def test_retries_use_exponential_backoff():
    delays: list[float] = []
    attempts = {"n": 0}

    def flaky() -> str:
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise LLMError("boom")
        return "ok"

    assert call_with_retries(flaky, max_retries=3, base_delay=1.0, sleep=delays.append) == "ok"
    assert delays == [1.0, 2.0]


def test_retries_give_up_after_limit():
    def always_fails() -> str:
        raise LLMError("boom")

    with pytest.raises(LLMError):
        call_with_retries(always_fails, max_retries=2, base_delay=0, sleep=NO_SLEEP)


def test_api_key_never_leaks(seeded, monkeypatch):
    """Ключ не попадает ни в repr провайдера, ни в generation_runs."""
    secret = "sk-super-secret-value"
    monkeypatch.setenv("LLM_API_KEY", secret)
    monkeypatch.setenv("LLM_MODEL", "gpt-test")
    monkeypatch.setenv("LLM_BASE_URL", "https://example.invalid/v1")

    provider = provider_from_env()
    assert isinstance(provider, OpenAICompatibleProvider)
    assert secret not in repr(provider)
    assert secret not in str(vars(provider).get("model", ""))

    mock = MockLLMProvider([expansion("pear")], model="gpt-test")
    expand_category(seeded, mock, category_key="fruits", count=1, batch_size=1)
    dump = "".join(
        str(value)
        for row in seeded.execute("SELECT * FROM generation_runs")
        for value in tuple(row)
    )
    assert secret not in dump


def test_provider_from_env_requires_key(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    with pytest.raises(LLMError):
        provider_from_env()


def test_mock_from_file_repeats_last(tmp_path):
    import json

    path = tmp_path / "mock.json"
    path.write_text(json.dumps(expansion("pear")), encoding="utf-8")
    provider = MockLLMProvider.from_file(path)

    first = provider.complete_json("prompt one")
    second = provider.complete_json("prompt two")
    assert first.text == second.text
    assert len(provider.calls) == 2


def test_echo_handler_shapes():
    assert echo_handler("category_key: fruits\n...") == {"category_key": "fruits", "candidates": []}
    assert echo_handler("some catalog prompt") == {"words": []}
    verdicts = echo_handler('[{"membership_id": 7}]')["verdicts"]
    assert verdicts[0]["membership_id"] == 7


def test_environment_variable_names_are_stable():
    from word_content.llm import openai_compatible as oc

    assert (oc.ENV_API_KEY, oc.ENV_BASE_URL, oc.ENV_MODEL) == (
        "LLM_API_KEY",
        "LLM_BASE_URL",
        "LLM_MODEL",
    )
    assert os.environ.get("LLM_API_KEY") is None or True  # тест не требует реального ключа
