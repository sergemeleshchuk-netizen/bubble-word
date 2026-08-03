import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { defineConfig, type Plugin } from 'vite';
import react from '@vitejs/plugin-react';

/**
 * Прототип на dev-сервере.
 *
 * Шаг «Прототип» открывает играбельный прототип относительным путём
 * `../playable/index.html`: на сайте инструмент и прототип лежат соседними
 * каталогами (`/tool/` и `/playable/`). В dev-сервере инструмент открыт из
 * корня, и такого соседа там нет — эта прослойка отдаёт тот самый файл из
 * `site/playable/`. Копию делать нельзя: прототип живёт в одном месте, и
 * вторая его версия начала бы тихо отставать.
 */
function playableInDev(): Plugin {
  const here = dirname(fileURLToPath(import.meta.url));
  const file = resolve(here, '../../site/playable/index.html');
  return {
    name: 'playable-in-dev',
    apply: 'serve',
    configureServer(server) {
      server.middlewares.use('/playable', (req, res, next) => {
        // прототип — один файл; остальное из /playable/ (packs/) в dev не нужно
        const path = (req.url ?? '/').split('?')[0];
        if (path !== '/' && path !== '/index.html') { next(); return; }
        try {
          const html = readFileSync(file);
          res.setHeader('Content-Type', 'text/html; charset=utf-8');
          res.end(html);
        } catch {
          next();
        }
      });
    },
  };
}

// Корень — web/, сборка в web/dist. Снимок базы импортируется как JSON и
// уезжает в бандл: инструмент работает без сервера, ключей и сети.
export default defineConfig({
  root: 'web',
  base: './',
  plugins: [react(), playableInDev()],
  build: { outDir: 'dist', emptyOutDir: true, chunkSizeWarningLimit: 3000 },
});
