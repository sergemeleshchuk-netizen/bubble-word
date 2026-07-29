from __future__ import annotations

import argparse
import itertools
import json
import math
import re
import time
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd
import requests
import yaml
from rapidfuzz.fuzz import ratio
from tenacity import retry, stop_after_attempt, wait_exponential
from wordfreq import zipf_frequency

WORD_RE = re.compile(r"^[a-z][a-z -]*[a-z]$|^[a-z]$")

@dataclass
class Group:
    group_id: str
    title: str
    relation_type: str
    source: str
    source_id: str
    words: list[str]
    source_url: str


def clean_word(text: str) -> str | None:
    word = text.strip().lower().replace("_", " ")
    word = re.sub(r"\s+", " ", word)
    if not WORD_RE.match(word):
        return None
    if any(ch.isdigit() for ch in word):
        return None
    return word


def load_wordnet() -> list[Group]:
    import nltk
    from nltk.corpus import wordnet as wn

    try:
        wn.ensure_loaded()
    except LookupError:
        nltk.download("wordnet", quiet=False)
        nltk.download("omw-1.4", quiet=False)

    groups: list[Group] = []
    seen = set()
    counter = 0
    for parent in wn.all_synsets(pos=wn.NOUN):
        children = parent.hyponyms()
        members = []
        for child in children:
            lemmas = [clean_word(x.name()) for x in child.lemmas()]
            lemmas = [x for x in lemmas if x]
            if lemmas:
                members.append(lemmas[0])
        members = sorted(set(members))
        if len(members) < 4:
            continue
        title = clean_word(parent.lemmas()[0].name()) or parent.name().split(".")[0]
        for combo in bounded_combinations(members, 4, 60):
            key = tuple(combo)
            if key in seen:
                continue
            seen.add(key)
            counter += 1
            groups.append(Group(
                group_id=f"WN-{counter:07d}",
                title=title,
                relation_type="is_a",
                source="WordNet",
                source_id=parent.name(),
                words=list(combo),
                source_url="https://wordnet.princeton.edu/",
            ))
    return groups


def bounded_combinations(items: list[str], size: int, limit: int) -> Iterable[tuple[str, ...]]:
    if len(items) <= 12:
        return itertools.islice(itertools.combinations(items, size), limit)
    # Deterministic windows avoid combinatorial explosion and preserve diversity.
    combos = []
    for offset in range(min(limit, len(items))):
        picks = [items[(offset + step * max(1, len(items) // size)) % len(items)] for step in range(size)]
        if len(set(picks)) == size:
            combos.append(tuple(sorted(picks)))
    return iter(dict.fromkeys(combos))


@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=2, min=2, max=30))
def http_json(url: str, *, params=None, headers=None, timeout=60):
    response = requests.get(url, params=params, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.json()


def load_wikidata(config: dict) -> list[Group]:
    endpoint = config["wikidata"]["endpoint"]
    headers = {"User-Agent": config["wikidata"]["user_agent"], "Accept": "application/sparql-results+json"}
    categories = {
        "musical instruments": "Q34379",
        "sports": "Q349",
        "fruits": "Q3314483",
        "vegetables": "Q11004",
        "professions": "Q28640",
        "vehicles": "Q42889",
        "dog breeds": "Q39367",
        "cat breeds": "Q43577",
        "countries": "Q6256",
        "chemical elements": "Q11344",
    }
    groups: list[Group] = []
    counter = 0
    for title, qid in categories.items():
        query = f'''SELECT DISTINCT ?item ?itemLabel WHERE {{
          ?item wdt:P31/wdt:P279* wd:{qid}.
          SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
        }} LIMIT 500'''
        data = http_json(endpoint, params={"query": query, "format": "json"}, headers=headers)
        words = []
        for row in data["results"]["bindings"]:
            label = clean_word(row["itemLabel"]["value"])
            if label:
                words.append(label)
        words = sorted(set(words))
        for combo in bounded_combinations(words, 4, 100):
            counter += 1
            groups.append(Group(
                group_id=f"WD-{counter:07d}", title=title, relation_type="instance_of",
                source="Wikidata", source_id=qid, words=list(combo),
                source_url=f"https://www.wikidata.org/wiki/{qid}"
            ))
        time.sleep(0.5)
    return groups


def load_conceptnet(config: dict, seeds: list[str]) -> list[Group]:
    endpoint = config["conceptnet"]["endpoint"]
    min_weight = float(config["conceptnet"]["min_weight"])
    groups: list[Group] = []
    counter = 0
    for seed in seeds:
        url = f"{endpoint}/query"
        data = http_json(url, params={"node": f"/c/en/{seed.replace(' ', '_')}", "limit": 100})
        related = []
        for edge in data.get("edges", []):
            if float(edge.get("weight", 0)) < min_weight:
                continue
            rel = edge.get("rel", {}).get("label", "")
            if rel not in {"RelatedTo", "AtLocation", "UsedFor", "HasProperty", "PartOf", "CapableOf"}:
                continue
            start = edge.get("start", {})
            end = edge.get("end", {})
            other = end if start.get("language") == "en" and start.get("label", "").lower() == seed else start
            if other.get("language") != "en":
                continue
            word = clean_word(other.get("label", ""))
            if word and word != seed:
                related.append((word, rel, edge.get("@id", "")))
        by_rel = defaultdict(list)
        for word, rel, edge_id in related:
            by_rel[rel].append(word)
        for rel, words in by_rel.items():
            words = sorted(set(words))
            for combo in bounded_combinations(words, 4, 20):
                counter += 1
                groups.append(Group(
                    group_id=f"CN-{counter:07d}", title=seed, relation_type=rel,
                    source="ConceptNet", source_id=seed, words=list(combo),
                    source_url=f"https://conceptnet.io/c/en/{seed.replace(' ', '_')}"
                ))
        time.sleep(0.2)
    return groups


def cefr_from_zipf(z: float) -> str:
    if z >= 5.2: return "A1"
    if z >= 4.7: return "A2"
    if z >= 4.2: return "B1"
    if z >= 3.7: return "B2"
    if z >= 3.2: return "C1"
    return "C2"


def score_groups(groups: list[Group], config: dict) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    word_group_count = Counter(w for g in groups for w in g.words)
    group_rows, word_rows, conflict_rows = [], [], []
    accepted_words = defaultdict(set)

    for g in groups:
        metrics = []
        for word in g.words:
            z = round(float(zipf_frequency(word, "en")), 2)
            ambiguity = word_group_count[word]
            metrics.append((word, z, ambiguity))
            accepted_words[word].add(g.group_id)

        avg_zipf = sum(x[1] for x in metrics) / 4
        min_zipf = min(x[1] for x in metrics)
        max_ambiguity = max(x[2] for x in metrics)
        length_penalty = sum(max(0, len(x[0]) - 10) for x in metrics) * 2
        phrase_penalty = sum(4 for x in metrics if " " in x[0])
        frequency_penalty = max(0, 4.5 - avg_zipf) * 12 + max(0, 3.2 - min_zipf) * 18
        ambiguity_penalty = min(35, max(0, max_ambiguity - 2) * 4)
        title_similarity = max(ratio(g.title, w) for w, _, _ in metrics)
        clarity_bonus = 8 if title_similarity >= 45 else 0
        risk_score = round(min(100, length_penalty + phrase_penalty + frequency_penalty + ambiguity_penalty - clarity_bonus), 1)
        if risk_score >= config["risk_threshold_reject"]:
            status = "REJECT"
        elif risk_score >= config["risk_threshold_review"]:
            status = "REVIEW"
        else:
            status = "SAFE_CANDIDATE"
        difficulty = round(min(10, 1 + (5.5 - avg_zipf) * 1.6 + phrase_penalty / 5 + ambiguity_penalty / 12), 1)
        group_rows.append({
            "group_id": g.group_id, "title": g.title, "relation_type": g.relation_type,
            "word_1": g.words[0], "word_2": g.words[1], "word_3": g.words[2], "word_4": g.words[3],
            "source": g.source, "source_id": g.source_id, "source_url": g.source_url,
            "avg_zipf": round(avg_zipf, 2), "min_zipf": round(min_zipf, 2),
            "cefr_est": cefr_from_zipf(avg_zipf), "max_word_ambiguity": max_ambiguity,
            "difficulty_score": difficulty, "risk_score": risk_score, "status": status,
            "metric_note": "Zipf from wordfreq; CEFR is heuristic, not an official CEFR label"
        })
        for word, z, ambiguity in metrics:
            word_rows.append({
                "word": word, "group_id": g.group_id, "group_title": g.title,
                "zipf": z, "cefr_est": cefr_from_zipf(z), "length": len(word),
                "group_memberships": ambiguity, "source": g.source, "source_id": g.source_id,
                "source_url": g.source_url
            })

    for word, ids in accepted_words.items():
        if len(ids) > 1:
            conflict_rows.append({"word": word, "group_count": len(ids), "group_ids": ", ".join(sorted(ids))})
    return pd.DataFrame(group_rows), pd.DataFrame(word_rows), pd.DataFrame(conflict_rows)


def export(groups_df: pd.DataFrame, words_df: pd.DataFrame, conflicts_df: pd.DataFrame, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    groups_df.to_csv(out_dir / "groups.csv", index=False)
    words_df.to_csv(out_dir / "words.csv", index=False)
    conflicts_df.to_csv(out_dir / "conflicts.csv", index=False)
    safe = groups_df[groups_df["status"] == "SAFE_CANDIDATE"].copy()
    safe.to_csv(out_dir / "safe_groups.csv", index=False)
    with pd.ExcelWriter(out_dir / "bubble_jam_database.xlsx", engine="openpyxl") as writer:
        groups_df.to_excel(writer, sheet_name="Groups", index=False)
        words_df.to_excel(writer, sheet_name="Words", index=False)
        conflicts_df.to_excel(writer, sheet_name="Conflicts", index=False)
        safe.to_excel(writer, sheet_name="Safe_Groups", index=False)
        pd.DataFrame([
            {"metric": "groups_total", "value": len(groups_df)},
            {"metric": "safe_candidates", "value": int((groups_df.status == 'SAFE_CANDIDATE').sum())},
            {"metric": "review", "value": int((groups_df.status == 'REVIEW').sum())},
            {"metric": "reject", "value": int((groups_df.status == 'REJECT').sum())},
            {"metric": "unique_words", "value": words_df.word.nunique()},
        ]).to_excel(writer, sheet_name="Summary", index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/settings.yaml")
    parser.add_argument("--output", default="output")
    parser.add_argument("--wordnet-only", action="store_true")
    args = parser.parse_args()
    config = yaml.safe_load(Path(args.config).read_text())
    groups = load_wordnet()
    if not args.wordnet_only and config["sources"].get("wikidata"):
        groups.extend(load_wikidata(config))
    if not args.wordnet_only and config["sources"].get("conceptnet"):
        seeds = ["beach", "school", "kitchen", "airport", "hospital", "garden", "winter", "music", "party", "office"]
        groups.extend(load_conceptnet(config, seeds))
    # Exact duplicate groups removed regardless of title/source.
    deduped = {}
    for g in groups:
        key = tuple(sorted(g.words))
        deduped.setdefault(key, g)
    groups_df, words_df, conflicts_df = score_groups(list(deduped.values()), config)
    export(groups_df, words_df, conflicts_df, Path(args.output))
    print(json.dumps({
        "groups": len(groups_df),
        "safe": int((groups_df.status == "SAFE_CANDIDATE").sum()),
        "review": int((groups_df.status == "REVIEW").sum()),
        "reject": int((groups_df.status == "REJECT").sum()),
        "unique_words": int(words_df.word.nunique()),
    }, indent=2))

if __name__ == "__main__":
    main()
