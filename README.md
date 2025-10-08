# Tim-Tam-Game
ティムタムゲーム

## ゲームの説明
「ティム」と「タム」がランダムに13回表示されます。14回目に何がくるかを当てるゲームです。

## 実行方法

### Reactアプリ版（推奨）

#### 開発モードで実行
```bash
npm install
npm run dev
```
ブラウザで `http://localhost:5173` を開いてください。

#### 本番ビルド
```bash
npm run build
npm run preview
```

### CLI版
```bash
python3 timtam_game.py
```

## 必要環境
- Node.js 18.x以上 (Reactアプリ用)
- Python 3.x (CLI版用)

**注意**: 正解は必ず回答の逆になります！
- 「ティム」と答えた場合 → 正解は「タム」
- 「タム」と答えた場合 → 正解は「ティム」
