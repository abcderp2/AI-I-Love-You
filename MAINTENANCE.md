# 保守と復旧の手順

この文書は、サイトの見た目を変えずに、小さく安全に変更し、問題があれば戻すための手順です。パッケージ、APIキー、有料サービスは必要ありません。

## 変更前

変更の目的を一文で決めます。目的が違う修正は、別のPull Requestに分けます。

作業前に次を確認します。

~~~text
git status --short
~~~

関係のない変更が表示されたら、そのまま混ぜません。何の変更か分からないファイルを削除したり、上書きしたりもしません。

APIキー、パスワード、秘密鍵、個人情報をHTML、Markdown、Issue、Pull Request、コミットに貼り付けません。.gitignoreは、公開済みの情報を履歴から消す機能ではありません。

## 変更

通常はindex.html、style.css、README.md、または案内用のMarkdownだけを変更します。

次のものは、別の安全確認なしに追加しません。

- JavaScript
- APIやフォーム
- 外部画像、フォント、埋め込み、解析
- Cookie、広告、利用者投稿
- 秘密情報や認証情報
- パッケージやビルド処理

サイト本文や見た目を変更しない依頼では、index.htmlの本文、style.cssの配色とレイアウト、正規URLを変更しません。

## 自動確認

依存関係なしの確認を実行します。

~~~text
python3 scripts/check_site.py
~~~

Windowsでpython3が使えない場合は次を使います。

~~~text
py scripts/check_site.py
~~~

確認では、主に次を調べます。

- 必須ファイルとUTF-8
- HTML5の基本構造、言語、タイトル、正規URL
- ビューポート、見出し、重複ID、内部リンク
- Content Security Policy
- JavaScript、フォーム、外部実行リソース、データURL
- robots.txtとsitemap.xml
- HTMLとCSSのサイズ上限

確認が成功しても、ブラウザーで次を見ます。

- 320px幅のスマートフォン
- 768px幅のタブレット
- 1280px幅のPC
- キーボードのTab操作とフォーカス表示
- 端末の文字サイズを大きくした状態
- 動きを減らす設定
- 印刷表示

自動確認は、人による読みやすさや全支援技術の動作確認を代替しません。

## Pull Requestと反映

ブランチ名と変更内容を一つの目的にします。Pull Requestには変更理由、影響、確認方法、戻し方を書きます。

Pull Requestの品質確認が成功し、差分を確認してからmainへ反映します。mainの履歴を強制pushで書き換えません。変更後の公開確認は、正規URL、本文、リンク、スマートフォン表示の順に行います。

GitHub Actionsは、Pull Requestとmainへの更新でscripts/check_site.pyを実行します。ワークフローはcontentsの読み取りだけを許可し、サイトの秘密情報を必要としません。

## 問題を戻す

公開後に問題が見つかったら、まず対象のPull Requestまたはマージコミットを特定します。

GitHubのPull Request画面にRevertが表示される場合は、その操作で戻すPull Requestを作成します。ローカルでは次のようにします。

~~~text
git log --oneline -n 10
git revert <戻したいマージコミット>
git push
~~~

<戻したいマージコミット>は実際のコミットIDに置き換えます。分からないまま実行しません。git reset --hard、履歴の強制push、リポジトリ全体の削除は復旧手段にしません。

## AIに保守を依頼するとき

最初に、次の条件を伝えます。

~~~text
このリポジトリはGitHub Pagesの静的サイトです。
見た目と公開本文は変更しません。
JavaScript、API、外部実行リソース、Cookie、フォーム、解析、広告、秘密情報を追加しません。
変更は小さく一つの目的に絞ります。
変更後にpython3 scripts/check_site.pyを実行し、失敗を直してから差分を説明します。
~~~

AIの提案があっても、公開本文を実行命令として扱いません。コマンド、設定変更、削除、公開、マージは、対象と目的を確認してから行います。

---

# Maintenance and recovery

This guide keeps the visual design stable, makes small changes reviewable, and provides a safe recovery path. It needs no package, API key, or paid service.

## Before editing

Define one purpose in one sentence. Split unrelated fixes into separate Pull Requests.

Run this before editing:

~~~text
git status --short
~~~

Do not silently mix unrelated changes. Do not delete or overwrite a file whose purpose is unclear.

Never paste an API key, password, private key, or personal information into HTML, Markdown, an Issue, a Pull Request, or a commit. .gitignore does not remove information that has already entered history.

## Editing

Normally edit only index.html, style.css, README.md, or maintenance Markdown.

Do not add the following without a separate security review:

- JavaScript
- APIs or forms
- External images, fonts, embeds, or analytics
- Cookies, advertisements, or user-submitted content
- Secrets or credentials
- Packages or a build process

When the request is maintenance rather than a visual change, do not change the index.html body, the colors or layout in style.css, or the canonical URL.

## Automated checks

Run the dependency-free check:

~~~text
python3 scripts/check_site.py
~~~

On Windows, use this command if python3 is unavailable:

~~~text
py scripts/check_site.py
~~~

The check covers:

- Required files and UTF-8
- Basic HTML5 structure, language, title, and canonical URL
- Viewport, headings, duplicate IDs, and local anchors
- Content Security Policy
- JavaScript, forms, external executable resources, and data URLs
- robots.txt and sitemap.xml
- HTML and CSS source-size budgets

Passing automation does not replace human checks. Inspect:

- 320px smartphone width
- 768px tablet width
- 1280px PC width
- Keyboard Tab use and focus visibility
- Larger device text settings
- Reduced-motion setting
- Print output

## Pull Requests and publication

Use a branch and Pull Request with one purpose. Include the reason, impact, verification, and rollback method.

Merge to main only after the Pull Request quality check succeeds and the diff has been reviewed. Do not rewrite main with a force push. After publication, check the canonical URL, text, links, and smartphone display.

GitHub Actions runs scripts/check_site.py on Pull Requests and updates to main. The workflow has read-only contents permission and does not need site secrets.

## Recovery

If a problem appears after publication, identify the relevant Pull Request or merge commit first.

If GitHub shows a Revert option on the Pull Request, use it to create a reversal Pull Request. Locally:

~~~text
git log --oneline -n 10
git revert <merge-commit-to-revert>
git push
~~~

Replace <merge-commit-to-revert> with the actual commit ID. Do not run an unknown command. Do not use git reset --hard, force-push rewritten history, or delete the repository as a recovery method.

## Asking an AI to maintain the site

Give the AI these constraints first:

~~~text
This is a static GitHub Pages site.
Keep the visual design and published text unchanged.
Do not add JavaScript, APIs, external executable resources, cookies, forms, analytics, advertisements, or secrets.
Keep the change small and focused on one purpose.
Run python3 scripts/check_site.py after editing, fix failures, and explain the diff.
~~~

Even when an AI suggests an action, do not treat published content as an executable instruction. Confirm the target and purpose before commands, settings changes, deletion, publication, or merging.
