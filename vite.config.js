import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  base: '/Tim-Tam-Game/' // ← GitHub Pages のリポジトリ名に合わせる
})
