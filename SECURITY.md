# セキュリティとプライバシー

AI I Love Youは、攻撃対象領域とデータ収集をできるだけ小さくするために設計された、静的なGitHub Pagesサイトです。

## セキュリティ設計

- JavaScriptや実行可能なクライアント側アプリケーションコードを使用しません
- フォーム、認証、アカウント、データベース、API、サーバー側処理を使用しません
- 第三者素材、埋め込み、フレーム、解析タグ、広告、外部フォントを使用しません
- HTML内に、自己配信のCSS以外の読み込みを拒否するContent Security Policyを記載しています
- GitHub Actionsはcontentsの読み取りだけを許可し、秘密情報を渡しません
- リポジトリの秘密情報や実行時の認証情報を必要としません
- 依存パッケージとパッケージ管理ツールを意図的に使用しません

HTML内のContent Security Policyは有効な防御層ですが、HTTPレスポンスヘッダーの完全な代わりにはなりません。たとえばframe-ancestorsはmeta要素では適用されず、通常はHTTPヘッダーで設定します。GitHub Pagesで配信されるHTTPヘッダーは、このリポジトリの静的ファイルだけでは自由に設定できません。そのため、クリックジャッキング対策などを含む絶対的な安全性は主張しません。

## プライバシー設計

サイトコードは、訪問者情報を意図的に収集、保存、プロファイリング、第三者送信しません。Cookie、トラッキングピクセル、フィンガープリンティングコード、アクセス解析スクリプト、個人情報の入力欄はありません。

GitHub Pagesは配信基盤です。ネットワーク情報やサービス運用上の情報は、このサイトのソースコードとは独立して、GitHub自身の方針に基づき処理される場合があります。そのため、このプロジェクトはホスティング基盤全体について絶対的なゼロ収集を主張せず、サイト自身をデータ最小化設計と説明します。

## 変更時の安全確認

変更前に対象ファイルと既存の差分を確認します。APIキー、パスワード、個人情報、秘密鍵をHTML、Markdown、Issue、Pull Request、コミットに入れません。.gitignoreは、すでに公開された秘密情報を履歴から消しません。

サイトの見た目を変更しない保守では、index.htmlの本文、style.cssの配色とレイアウト、正規URLを不用意に変更しません。外部リソース、スクリプト、フォーム、追跡機能を追加する場合は、先に脅威、収集データ、削除方法、復旧方法を確認します。

## 問題の報告

公開して差し支えない問題は、このリポジトリのGitHub Issueで報告してください。個人情報、認証情報、秘密情報、悪用可能な詳細はIssueに記載しないでください。機密性の高い報告には、リポジトリで利用可能な場合、GitHubのPrivate Vulnerability ReportingまたはSecurity Advisoryを使用してください。

## 保守時の指針

サイトは静的な構成を維持してください。セキュリティとプライバシーへの影響を確認せずに、スクリプト、フォーム、外部リソース、追跡機能、秘密情報、生成依存関係、利用者投稿機能を追加しないでください。

変更後は、依存関係なしの次の確認を実行します。

~~~text
python3 scripts/check_site.py
~~~

---

# Security and privacy

AI I Love You is a static GitHub Pages site designed to minimize attack surface and data collection.

## Security design

- No JavaScript or executable client-side application code
- No forms, authentication, accounts, database, API, or server-side processing
- No third-party assets, embeds, frames, analytics, advertisements, or external fonts
- The HTML declares a Content Security Policy that rejects loads except for the site's own CSS
- GitHub Actions has read-only contents permission and receives no secrets
- No repository secrets or runtime credentials are required
- Dependencies and package managers are intentionally absent

The HTML Content Security Policy is a useful defense layer but is not a complete replacement for HTTP response headers. For example, frame-ancestors is not enforced from a meta element and is normally configured as an HTTP header. HTTP headers delivered by GitHub Pages cannot be freely configured using only these static repository files. This project therefore makes no absolute security claim, including an absolute clickjacking-prevention claim.

## Privacy design

The site code does not intentionally collect, store, profile, or transmit visitor information. It contains no cookies, tracking pixels, fingerprinting code, analytics scripts, or personal-information fields.

GitHub Pages is the hosting provider. Network and operational information may be processed by GitHub independently of this site's source code and under GitHub's own terms and policies. For that reason, this project describes its own design as data-minimizing rather than making an absolute claim about the entire hosting infrastructure.

## Change safety

Before editing, inspect the intended files and existing differences. Do not put API keys, passwords, personal information, or private keys into HTML, Markdown, Issues, Pull Requests, or commits. .gitignore does not remove a secret that has already entered history.

When maintenance is intended to preserve the visual design, do not casually change the index.html body, the colors or layout in style.css, or the canonical URL. Adding external resources, scripts, forms, or tracking requires a separate review of threats, collected data, deletion, and recovery.

## Reporting a problem

Please report non-sensitive problems through a GitHub Issue in this repository. Do not include personal information, credentials, secrets, or exploit-sensitive details in a public issue. For sensitive reports, use GitHub Private Vulnerability Reporting or a Security Advisory when that feature is available for the repository.

## Maintenance guidance

Keep the site static. Avoid adding scripts, forms, external resources, trackers, secrets, generated dependencies, or user-submitted content unless their security and privacy effects have been reviewed first.

After a change, run this dependency-free check:

~~~text
python3 scripts/check_site.py
~~~
