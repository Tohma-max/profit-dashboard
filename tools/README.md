# 生活ツール

claude.ai の Artifact として公開しているツールのソース置き場。
各 HTML は Artifact のページ本体で、`<!doctype html>` や `<head>` などの外枠は公開時に claude.ai が付ける。

| ツール | ファイル | 内容 |
|---|---|---|
| 完済コックピット | `money-cockpit/cockpit.html` | カードローン・家族からの借入の返済管理、特別損益（ギャンブル・デイトレ）の記録、ボーナス配分 |
| FP2・簿記2級 合格ノート | `study-hub/study.html` | 試験日からの学習時間の逆算、通勤学習の記録、分野別の正答率と次にやる分野、簿記2級の計算ドリル |

## データの置き場所

- 記録は claude.ai 側のデータベース（Artifact の db 機能）に保存し、このリポジトリには入れない。
- 読み書きできるのは Artifact の所有者だけ（アクセスルール `read: owner / write: owner`）。
- claude.ai の外でファイルを直接開いた場合は、そのブラウザの localStorage に保存する。
