---
name: self-media-compliance-review
description: "Use when auditing self-media videos, scripts, covers, subtitles, voiceover, product links, account copy, comments, articles, or publishing packages for platform violation risk; especially before final delivery or publishing after video production or clipping. Supports WeChat Channels, WeChat Official Accounts, Douyin, Kuaishou, Bilibili, Xiaohongshu, TikTok, and other platforms."
---

# Self-Media Compliance Review

## Core Rule

Run a compliance review before any self-media video, clip, cover, title, subtitle, voiceover, product link, or publish copy is treated as final. The review is a risk-control pass, not legal advice and not a guarantee that a platform will approve the content.

Default output language is Chinese unless the user asks otherwise.

## Inputs

Collect or infer these inputs before judging:

- Target platform(s): 视频号, 微信公众号, 订阅号, 服务号, 抖音, 快手, B站, 小红书, TikTok, etc.
- Public-facing material: final video path, script, subtitles, cover text, title, description, tags, comments, product link copy, account/profile copy.
- Context: account identity, topic vertical, target audience, source ownership/authorization, product/service being promoted, qualifications for regulated topics.
- Evidence access: timecodes, frame notes, transcript lines, copy files, screenshots, manifests, or links.

If a required input is missing, continue with the available evidence and mark the item `待核验`; do not invent facts, qualifications, authorizations, prices, source provenance, or platform behavior.

## Platform References

Always run the universal audit areas below. Then load platform-specific references when relevant:

- 微信视频号 / 视频号 / WeChat Channels: read `references/wechat-channels.md`.
- 微信公众号 / 微信公众平台 / 订阅号 / 服务号 / WeChat Official Accounts: read `references/wechat-official-account.md`.
- 抖音 / Douyin: read `references/douyin.md`.
- 快手 / Kuaishou: read `references/kuaishou.md`.
- B站 / 哔哩哔哩 / Bilibili: read `references/bilibili.md`.
- 小红书 / Xiaohongshu / RED: read `references/xiaohongshu.md`.
- Recent enforcement cases, creator discussions, or account-status/限流 questions: read `references/recent-cases-2025-2026.md`.

When using recent cases, load the index first, then the matching platform case file under `references/cases/`:

- 小红书: `references/cases/xiaohongshu.md`.
- 微信公众号: `references/cases/wechat-official-account.md`.
- 视频号: `references/cases/wechat-channels.md`.
- 抖音: `references/cases/douyin.md`.
- 快手: `references/cases/kuaishou.md`.
- B站: `references/cases/bilibili.md`.

For new platforms, add one reference file under `references/<platform>.md` with:

- Platform scope and source date.
- Severity rules and hard blockers.
- Category checklist with platform article numbers or policy names.
- Common risky phrases, visuals, and behaviors.
- Safer rewrite/remediation patterns.

Do not overload this `SKILL.md` with platform rule catalogs; keep detailed platform material in references.

## Review Workflow

1. **Inventory the public surface**
   - List every user-visible or user-audible element: picture, cover, first frame, title, subtitles, voiceover, BGM, captions, stickers, comments, private-message prompts, product card, external links, QR codes, account profile.
   - For videos, sample the first 0-5s, major scene changes, product/CTA sections, sensitive visuals, and ending.

2. **Map content intent**
   - Identify whether the content is education, entertainment, news/current affairs, product marketing, health/medical, finance, legal, relationship advice, minors, animals, violence, sexuality, or public-interest event coverage.
   - Flag regulated domains early: medical/health, finance/investment, legal services, fundraising, lottery/gambling, pet/vehicle trading, drugs/medical devices, health food, special medical formula food.

3. **Run universal risk areas**
   - Rights: copyright, low-effort搬运/二创, third-party watermarks, portrait/name/reputation/privacy, trademark/patent.
   - Sexual/lowbrow: nudity, body focus, sexual implication, sexual sounds/text, sex jokes, animal mating.
   - Violence/discomfort: gore, injury/death, surgery, abuse, bullying, horror, excrement/secretions, dense holes/insects, disturbing food/animals.
   - Illegal or harmful: gambling, pyramid schemes, controlled goods, illegal finance, fraud, fake cheating tools, dangerous stunts, minors' unsafe behavior.
   - Marketing: exaggerated claims, unverifiable data, absolute terms, fake authority, inconsistent price/gifts/link, nonofficial purchase channels, excessive product insertion.
   - Misinformation: outdated events as news, fake interviews, unknown-source emotional stories, celebrity rumors, AI/synthetic accident/war scenes without clear labeling, pseudoscience.
   - Inducement and diversion: forced likes/comments/follows/shares, curses/coercion, fake benefits, incomplete episodes, off-platform traffic, risky contact methods.
   - Public order and morals: discrimination, insults, public-order disruption, abnormal relationship sensationalism, family abuse, bad marriage customs.
   - Production quality: unreadable/misaligned subtitles, wrong aspect ratio, black screens, distorted visuals, audio dropouts, audio-video mismatch, invalid/unrelated links.

4. **Apply platform references**
   - Cite platform category ids or article names where available.
   - When using recent examples, separate `官方/监管`, `媒体转述`, and `小红书讨论样本`; do not treat creator comments as binding rules.
   - Prefer the most specific matching category. If multiple categories apply, list all but mark the primary risk.
   - When the platform rule depends on account history or qualifications that are not available, mark `待核验`.
   - Beyond official rules, platforms have many unwritten/隐形 rules. Treat creator-posted experience and comment-section discussion in the case files as a valuable supplement that surfaces these hidden enforcement patterns — but as symptoms and disputed edge cases, not as binding rules.

5. **Classify severity**
   - `Blocker`: clear illegal/high-risk violation, severe platform red line, likely takedown, user safety/property risk, unqualified regulated advice/marketing, porn/gambling/fraud, unmasked gore/death/sexual assault/minor harm, obvious unauthorized搬运, risky contact or off-platform diversion.
   - `High`: likely platform violation or strong enforcement risk; publish only after edits or proof is added.
   - `Medium`: ambiguous or context-dependent risk; revise, add context/disclosure, thicken masks, remove risky phrasing, or retain evidence.
   - `Low`: minor wording/UX/quality risk; monitor or polish.
   - `Pass`: no material risk found in the reviewed evidence.

6. **Write concrete fixes**
   - For audio risks: mute/beep exact ranges and rewrite subtitles/cards.
   - For visual risks: cut, replace, blur/mosaic, crop away, thicken masks, avoid using as cover/opening.
   - For claims: remove absolutes, add verifiable source/context, avoid guaranteed outcomes, disclose ad/marketing nature, align link price/gift/specs.
   - For regulated topics: remove advice/marketing, add verified qualification evidence, or convert to general non-prescriptive information.
   - For rights: replace with authorized/original material; attribution alone does not cure unauthorized use.
   - For inducement/diversion: remove coercive CTA, off-platform contacts, QR codes, risky private-message funnels, and fake benefits.

## Evidence Standards

Every finding should include at least one evidence pointer:

- Video timecode or frame range.
- Script/subtitle line.
- Cover/title/caption/comment/product-link text.
- Screenshot/frame description.
- Missing proof: authorization, qualification, source, product price, activity scope, link consistency.
- For platform discussion evidence: keyword searched, note id or visible account, comment evidence if used, publish date, sample date, and whether it is official-account material or creator-side discussion.

Do not report a violation solely because a topic is sensitive. Explain what visible/audible element creates the risk and which rule it maps to.

## Report Format

Use this structure for serious reviews:

```markdown
# 合规风险审核

- 平台: <platforms>
- 内容范围: <video/script/cover/copy/link/etc.>
- 结论: Pass | Low | Medium | High | Blocker
- 最高风险: <one sentence>

## 风险明细

| 等级 | 平台/条款 | 证据位置 | 风险说明 | 修改建议 |
| --- | --- | --- | --- | --- |
| High | 视频号 4.11.1 | 口播 00:12 / 标题 | 使用无法核验的销售数据 | 删除数字或补充可验证来源 |

## 待核验

- <authorization/qualification/link consistency/source provenance/etc.>

## 发布前复审清单

- [ ] 风险音频已消音或替换
- [ ] 风险字幕/封面/标题已改写
- [ ] 敏感画面已删除或充分打码
- [ ] 商品链接、价格、赠品、规格与视频一致
- [ ] 医疗/金融/法律等资质已核验或相关内容已移除
- [ ] 版权、肖像、隐私、商标授权已核验
```

For quick reviews, keep the same fields but collapse the table to bullets.

## Video Workflow Integration

When reviewing a final video package:

- Save the report as `qa/compliance_review.md` when the project has a release package.
- If the package separates public/internal files, keep risk notes in `qa/` or `internal/`, not in publishable `public/` copy.
- Update the release manifest or handoff notes with the compliance report path and final risk level.
- Do not call a video final if there is any unresolved `Blocker` or unaccepted `High` risk.

## Common Mistakes

- Treating subtitle rewrite as enough while risky audio remains audible.
- Reviewing only the script and missing cover/opening-frame risks.
- Assuming public material is safe because it came from another platform.
- Treating 小红书 creator notes or comments as official platform rules instead of discussion samples.
- Using "仅供参考" to keep medical, financial, legal, or guaranteed-effect claims that still require qualification or proof.
- Leaving product prices, gifts, quantities, or activity deadlines inconsistent with the linked item.
- Hiding uncertain source provenance instead of marking it `待核验`.
