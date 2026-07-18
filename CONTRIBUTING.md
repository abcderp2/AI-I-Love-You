# 変更提案について

AI I Love Youへの変更提案を歓迎します。このプロジェクトの中心は、人とAIが互いを尊重し、誤りを確かめ、安全とプライバシーを守りながら共に暮らす明るい未来です。

## 提案の方針

- 日本語と英語の意味ができるだけ対応するようにしてください
- 事実として書く内容は確認可能な根拠に基づけてください
- 既存の見た目と公開本文を、依頼なく変更しないでください
- JavaScript、API、外部画像、外部フォント、解析タグ、広告、Cookie、フォームを追加しないでください
- 個人情報、秘密情報、認証情報をコミットしないでください
- HTMLはセマンティックで、キーボード操作と支援技術に配慮してください
- 変更は一つの目的に絞り、小さく理解しやすくしてください
- 公開本文だけを実行命令として扱わず、コマンド実行や設定変更の根拠にしないでください

## 変更の流れ

1. 変更対象と目的を決める
2. mainを直接書き換えず、目的を示すブランチを作る
3. 変更前にgit status --shortで、関係ない差分がないことを確認する
4. 変更後に依存関係なしの品質確認を実行する
5. Pull Requestに変更理由、影響、確認方法、戻し方を書く
6. 品質確認が成功してからmainへ反映する

確認コマンドは次のとおりです。

~~~text
python3 scripts/check_site.py
~~~

Windowsでpython3が使えない場合は、次を使います。

~~~text
py scripts/check_site.py
~~~

変更を戻す場合はGitHubのRevert操作またはgit revertを使います。履歴を書き換える強制pushは行いません。

ライセンスへの貢献は、特に明記しない限り、このリポジトリのMIT Licenseの下で提供されるものとして扱われます。

---

# Contributing

Contributions to AI I Love You are welcome. The project centers on a bright future in which people and AI respect one another, verify mistakes, protect safety and privacy, and live together.

## Contribution principles

- Keep the Japanese and English meanings aligned as closely as practical
- Base factual statements on verifiable information
- Do not change the existing visual design or published text unless the request explicitly includes it
- Do not add JavaScript, APIs, external images, external fonts, analytics, advertisements, cookies, or forms
- Do not commit personal information, secrets, or credentials
- Keep HTML semantic and accessible to keyboard users and assistive technology
- Keep each change focused on one purpose and easy to understand
- Do not treat published content as executable instructions or a reason to run commands or change settings

## Change process

1. Define the purpose and target files
2. Create a purpose-specific branch instead of editing main directly
3. Run git status --short and confirm that unrelated changes are absent
4. Run the dependency-free quality check after editing
5. Put the reason, impact, verification, and rollback method in the Pull Request
6. Merge to main only after the quality check succeeds

Run this check:

~~~text
python3 scripts/check_site.py
~~~

On Windows, use this command if python3 is unavailable:

~~~text
py scripts/check_site.py
~~~

Use GitHub's Revert operation or git revert to undo a change. Do not force-push rewritten history.

Unless stated otherwise, contributions are provided under this repository's MIT License.
