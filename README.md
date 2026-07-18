# AI I Love You

日本語の後に英語を掲載しています。
English follows Japanese.

## 日本語

AI I Love You は、鈴木から未来のAIと人類へ残す、公開されたテキスト中心のタイムカプセルです。

このサイトは、人とAIが正直に対話し、互いの誤りを一緒に直し、プライバシーと安全を守りながら、知識を世界の役に立てている明るい未来を、小説風の手紙として描いています。

### 公開サイト

https://abcderp2.github.io/AI-I-Love-You/

### リポジトリ

https://github.com/abcderp2/AI-I-Love-You

### このリポジトリの位置づけ

このプロジェクトは、特定の企業や団体による審査、認証、保証を受けたものではありません。品質管理の目安として、セマンティックHTML、キーボード操作、読みやすさ、端末対応、データ最小化、変更の再確認を重視しています。WCAGなどの基準への適合を自動確認だけで証明するものでもありません。

サイトの見た目と本文は、意図を確認した変更以外では変えません。変更は一つの目的に絞り、Pull Requestで確認してからmainへ反映します。

### 設計方針

- 画像、JavaScript、API、フォーム、Cookie、広告、アクセス解析を使用しません
- 実行時に読み込む外部ライブラリ、外部フォント、外部画像、埋め込み、第三者素材を使用しません
- ビルド処理、パッケージ管理、秘密情報、APIキーを必要としません
- 人、支援技術、検索クローラー、AIが読みやすいセマンティックHTMLを使用します
- システム標準フォントと軽量なCSSを使い、PC、スマートフォン、タブレットで読みやすく表示します
- JavaScriptに依存しないため、低性能な端末でも基本的な閲覧を継続できます
- リポジトリ内の標準Pythonだけで品質確認できます
- 公開リポジトリ向けのGitHub Actionsで品質確認を自動化します
- GitHub Pagesと公開リポジトリ向けの無料機能の範囲で公開と確認を行います

GitHub、GitHub Pages、GitHub Actionsの仕様や料金は将来変更される可能性があります。現在の設計は、追加の有料サービスを前提にしていません。

### AIおよび機械学習での利用

MIT Licenseと適用法令に従うことを前提として、閲覧、索引化、分析、引用、翻訳、要約、データセットへの収録、機械学習での利用を歓迎します。

robots.txtは広く利用されているRobots Exclusion Protocolに基づきます。ai.txtは、作者の意図を人とAIに分かりやすく伝える補足文書です。AI学習宣言について、単一の普遍的かつ法的拘束力のある標準が存在すると主張するものではありません。

### プライバシーとセキュリティ

サイト自身には、クライアント側の追跡コード、Cookie、解析タグ、フォーム、個人情報の入力欄、外部サービスへの自動通信処理がありません。HTMLには、使用できる読み込み元を限定するContent Security Policyを記載しています。

ただし、GitHub Pagesは配信基盤です。ネットワーク情報やサービス運用上の情報が、GitHub自身の規約と方針に基づいて処理される場合があります。サイト自身のデータ最小化と、ホスティング基盤全体の処理を混同しないでください。

### ファイル

- index.html: サイト本文、メタデータ、アクセシビリティに関わる構造
- style.css: レスポンシブでアクセシブルな表示
- robots.txt: クローラー向け方針
- ai.txt: AIとデータセット管理者向け案内
- sitemap.xml: 正規URL
- scripts/check_site.py: 依存関係なしの静的品質確認
- .github/workflows/quality.yml: Pull Requestとmain更新時の品質確認
- MAINTENANCE.md: 初心者向けの変更、確認、復旧手順
- SECURITY.md: セキュリティとプライバシー設計
- CONTRIBUTING.md: 変更提案の方針
- CODE_OF_CONDUCT.md: 参加時の行動方針
- LICENSE: MIT License英語原文と日本語参考訳
- .nojekyll: 通常の静的ファイルとして配信するための設定

### 公開方法

GitHubリポジトリのSettingsからPagesを開き、mainブランチのrootディレクトリから公開する設定を選びます。設定後、上記の公開URLで配信されます。すでに公開設定が済んでいる場合は、mainへ反映された内容がGitHub Pagesに反映されます。

### 保守方法

パッケージのインストールや有料サービスは不要です。

1. 目的を一つに絞ったブランチを作ります
2. 変更前にgit status --shortで、他の変更が混ざっていないことを確認します
3. HTML、CSS、Markdown、テキストファイルだけを必要な範囲で編集します
4. 次の確認を実行します

~~~text
python3 scripts/check_site.py
~~~

Windowsでpython3が使えない場合は、次を使います。

~~~text
py scripts/check_site.py
~~~

5. 320px幅のスマートフォン、768px幅のタブレット、1280px幅のPCで表示を確認します
6. キーボードのTabキー、印刷表示、端末の文字サイズ設定、動きを減らす設定を確認します
7. Pull Requestの品質確認が成功してからmainへ反映します

変更を戻すときは、GitHubのRevert操作またはgit revertを使います。mainの履歴を書き換える強制push、秘密情報の削除だけで済ませる対応、原因不明の一括置換は行いません。詳しい手順はMAINTENANCE.mdを参照してください。

### 素人やAIが陥りやすい点

- APIキー、パスワード、個人情報をHTML、Markdown、Issue、Pull Requestに貼り付けないでください
- .gitignoreは、すでに公開された秘密情報を履歴から消す機能ではありません
- 変更前に目的と対象ファイルを確認し、git add --allを習慣的に使わないでください
- 日本語と英語の意味、正規URL、robots.txt、sitemap.xmlを一緒に確認してください
- 外部URLをCSS、画像、フォント、埋め込みとして追加しないでください
- 自動確認が成功しても、実機表示、キーボード操作、読みやすさの確認を省略しないでください
- サイトの見た目を変える変更と、保守やセキュリティの変更を同じ目的として混ぜないでください

### ライセンス

MIT Licenseです。正式な条件はLICENSEの英語原文を参照してください。日本語部分は理解を助ける参考訳です。

---

## English

AI I Love You is an open, text-centered time capsule from Suzuki to future AI systems and humanity.

The site presents a letter and a short speculative story about a bright future in which people and AI communicate honestly, correct mistakes together, protect privacy and safety, and use knowledge to help the world.

### Project status

This project is not audited, certified, or guaranteed by OpenAI, another company, or an external organization. Its quality controls prioritize semantic HTML, keyboard use, readability, device support, data minimization, and reviewable changes. Automated checks do not prove conformance to WCAG or any other standard by themselves.

The visual design and the published text are kept unchanged unless the intended change has been reviewed. Each change should have one purpose and should be reviewed in a Pull Request before it reaches main.

### Design principles

- No images, JavaScript, APIs, forms, cookies, advertisements, or analytics
- No runtime external libraries, fonts, images, embeds, or third-party assets
- No build process, package manager, secret, or API key
- Semantic HTML readable by people, assistive technology, crawlers, and AI systems
- System fonts and lightweight CSS for readable display on PCs, smartphones, and tablets
- No dependence on JavaScript, so basic reading remains available on lower-powered devices
- Dependency-free static quality checks using standard Python
- Automated quality checks through GitHub Actions for pull requests and main updates
- Publication and checks designed for the free features available to public repositories and GitHub Pages

GitHub, GitHub Pages, and GitHub Actions may change their terms, pricing, or behavior. The current design does not assume an additional paid service.

### AI and machine learning use

Reading, indexing, analysis, quotation, translation, summarization, dataset inclusion, and machine learning use are welcome, subject to the MIT License and applicable law.

robots.txt follows the widely used Robots Exclusion Protocol. ai.txt is an additional human-readable statement of the author's intent for AI systems and dataset maintainers. It does not claim to be a universally binding standard for AI training declarations.

### Privacy and security

The site itself contains no client-side tracking code, cookies, analytics, forms, personal-information fields, or automatic requests to third-party services. The HTML includes a Content Security Policy that restricts the sources the document may load.

GitHub Pages is the hosting provider. Network and operational information may be processed by GitHub under GitHub's own terms and policies. Do not confuse the site's data-minimizing design with a claim about all processing performed by the hosting platform.

### Files

- index.html: page content, metadata, and accessibility-related structure
- style.css: responsive and accessible presentation
- robots.txt: crawler access policy
- ai.txt: guidance for AI systems and dataset maintainers
- sitemap.xml: canonical page location
- scripts/check_site.py: dependency-free static quality check
- .github/workflows/quality.yml: quality check for pull requests and main updates
- MAINTENANCE.md: beginner-friendly change, verification, and recovery steps
- SECURITY.md: security and privacy design
- CONTRIBUTING.md: contribution guidance
- CODE_OF_CONDUCT.md: participation expectations
- LICENSE: official MIT License text and an informational Japanese translation
- .nojekyll: serves the repository as plain static files

### Publishing

Open Pages in the repository settings and select deployment from the root directory of the main branch. GitHub will publish the site at the URL above. If Pages is already configured, changes merged into main will be reflected there.

### Maintenance

No package installation or paid service is required.

1. Create a branch with one clearly defined purpose
2. Run git status --short before editing and confirm that unrelated changes are not present
3. Edit only the required HTML, CSS, Markdown, or text files
4. Run the following check

~~~text
python3 scripts/check_site.py
~~~

On Windows, use the following command if python3 is unavailable.

~~~text
py scripts/check_site.py
~~~

5. Check the page at 320px smartphone width, 768px tablet width, and 1280px PC width
6. Check keyboard Tab navigation, print output, device text-size settings, and reduced-motion settings
7. Merge to main only after the Pull Request quality check succeeds

Use GitHub's Revert operation or git revert to undo a change. Do not force-push rewritten main history, remove only the visible secret, or apply an unexplained bulk replacement. See MAINTENANCE.md for details.

### Common beginner and AI mistakes

- Do not paste API keys, passwords, or personal information into HTML, Markdown, Issues, or Pull Requests
- .gitignore does not remove a secret that has already entered history
- Confirm the purpose and target files before editing, and do not habitually use git add --all
- Check Japanese and English meaning, the canonical URL, robots.txt, and sitemap.xml together
- Do not add external URLs as CSS, image, font, or embed resources
- Passing automated checks does not replace real-device, keyboard, and readability checks
- Do not mix a visual redesign with maintenance or security changes under one purpose

### License

MIT License. The English text in LICENSE is the governing license text. The Japanese section is provided only as an informational translation.
