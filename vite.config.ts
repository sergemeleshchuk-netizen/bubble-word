import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Корень — web/, сборка в web/dist. Снимок базы импортируется как JSON и
// уезжает в бандл: инструмент работает без сервера, ключей и сети.
export default defineConfig({
  root: 'web',
  base: './',
  plugins: [react()],
  build: { outDir: 'dist', emptyOutDir: true, chunkSizeWarningLimit: 3000 },
});
