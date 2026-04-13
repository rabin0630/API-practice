

# 郵便番号検索 API アプリ (Vite + Vanilla JS + Tailwind v4)

外部の郵便番号検索 API（zipcloud）を利用し、入力された郵便番号から住所を動的に取得・表示するアプリケーション。

## プロジェクトの目的
- **JS 基礎の習得**: `fetch` API を用いた非同期通信と、`textContent` による動的な DOM 操作の実装。
- **最新開発環境の経験**: Vite 6 と Tailwind CSS v4 を組み合わせた、高速なビルド環境の構築。
- **実務的な UI 制御**: JavaScript による「7桁制限」バリデーションと、Tailwind によるレスポンシブな中央寄せレイアウトの実装。

## 使用技術
- **Build Tool**: Vite 6
- **Styling**: Tailwind CSS v4
- **API**: [zipcloud 郵便番号検索API](http://zipcloud.ibsnet.co.jp/doc/api)

## 開発環境の実行方法

### 前提条件
- **Node.js**: v24.14.1 以上
- **npm**: v10.9.x 以上

### 1. 依存パッケージのインストール
プロジェクトのルートディレクトリで以下を実行。

```bash
npm install
```

### 2. 開発用サーバーの起動
ローカル環境でプレビューを確認する場合。

```bash
npm run dev
```

### 3. 本番用ビルド
```bash
npm run build
```

## 実装のポイント
- **入力文字数制限**: `input` イベントを監視し、7桁を超える入力を `slice` メソッドで強制的に切り捨てるロジックを実装。
- **CSS-first スタイリング**: Tailwind v4 の指針に基づき、`style.css` へのインポートと Vite プラグインによる高速なスタイリングを採用。
- **視認性の向上**: 入力値および API 取得結果に `font-light` を適用し、モダンで洗練されたテキスト表示に調整。

## ディレクトリ構成
```text
.
├── index.html       # アプリのメイン構造
├── src/
│   ├── main.js      # API 通信・DOM 操作ロジック
│   └── style.css    # Tailwind インポート・カスタムスタイル
├── vite.config.js   # Tailwind プラグイン設定
└── package.json     # 依存ライブラリ管理
```

