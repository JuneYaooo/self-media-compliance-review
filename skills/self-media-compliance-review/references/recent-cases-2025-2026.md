# Recent Violation Cases and Platform Discussions

Use this index when a review would benefit from recent enforcement examples, creator pain points, or traceable case analogies.

Source audit date: 2026-06-20. Latest case-sample pass: 2026-06-23 (added native platform samples + an expanded Xiaohongshu official-governance-note catalog).

Primary window: 2025-06-20 through 2026-06-20. Older policy background or discussion samples should be used only when no newer source conflicts with them, and should be marked `older/context only`.

## Source Hierarchy

Use sources in this order:

1. Official platform rules, agreements, help-center pages, and official governance-account posts.
2. Government regulator notices and official campaign summaries.
3. Reputable media reports that quote official platform announcements or governance events.
4. Xiaohongshu search results and comments as creator discussion samples.

Do not treat Xiaohongshu creator notes or comments as binding platform rules. Use them to identify practical symptoms, disputed edge cases, and remediation questions to ask.

## Why User Discussions Matter (Hidden Rules)

Official rules cover only part of how platforms actually enforce. Much of the real risk lives in unwritten/隐形 rules that creators only discover after a note is limited, a video is taken down, or an appeal fails. Because of this, creator-posted experience and comment-section discussion are a valuable supplement to official sources:

- They surface enforcement patterns that official docs do not spell out (e.g. ordinary 经验分享 judged as 夸大其词, original work judged 原创性不足, 带货挂车后流量骤降).
- They show which appeal approaches and wordings work or fail in practice.
- They reveal disputed edge cases worth marking `待核验` rather than asserting.

Treat these as symptoms and leads, not rules. The platform case files include curated samples of such discussions with note/video ids and sample dates so findings stay traceable. Refresh them periodically, since counts, comments, and visibility drift over time.

Xiaohongshu doubles as the main *cross-platform* discussion venue: creators on 抖音/快手/视频号/公众号/B站 often post their 违规/限流/封号/申诉 experiences as Xiaohongshu notes. The per-platform case files therefore include "Xiaohongshu Discussion Samples About <platform>" sections sourced this way (cite as `案例库 小红书讨论样本 <date> <platform> <topic> note <id>`).

### 流量恢复玄学 / "复制一遍真有用" (cross-platform comment phenomenon)

A very high-volume pattern across platforms (sampled 2026-06-23 on Xiaohongshu): notes titled `复制一遍真有用` / `流量恢复楼` collect thousands of identical pasted comments like `没流量复制一遍真有用！您好，我近期注意到账号流量异常……恳请核查恢复流量` (representative notes `6a15c55f00000000360199e6` ~💬13501, `6a098e15000000003502d42d` ~💬11462, `697f5c1e0000000022023005`). Creators believe copy-pasting a fixed "求恢复" script restores traffic.

Review implication:

- This is engagement-manipulation/玄学, not a real recovery method. Do not advise it; platforms may treat coordinated identical comments as manipulation.
- Treat mass-identical comment chains (and the cross-platform `卸载去发小红书` venting复读) as noise/manipulation, not evidence of a specific violation.

When citing a case in a review, label it as:

- `案例库 官方/监管 <date> <topic>` for official or regulator material.
- `案例库 媒体转述 <date> <platform> <topic>` for reputable media quoting platform material.
- `案例库 小红书讨论样本 <date> <platform> <keyword>` for Xiaohongshu search results or comments.

## Platform Case Files

Load only the case file relevant to the review target:

- 小红书 / Xiaohongshu: read `cases/xiaohongshu.md`.
- 微信公众号 / 微信公众平台 / 订阅号 / 服务号: read `cases/wechat-official-account.md`.
- 微信视频号 / 视频号 / WeChat Channels: read `cases/wechat-channels.md`.
- 抖音 / Douyin: read `cases/douyin.md`.
- 快手 / Kuaishou: read `cases/kuaishou.md`.
- B站 / 哔哩哔哩 / Bilibili: read `cases/bilibili.md`.

If the user asks a cross-platform question such as `各个平台违规怎么办`, `限流怎么办`, or `封号申诉`, load the relevant platform files rather than this index alone.

Each platform case file should include `Scenario Playbooks` with:

- The concrete situation or symptom.
- Likely causes to check.
- Evidence and screenshots to collect.
- What to fix before appeal.
- How to structure an appeal.
- What not to do.

## Cross-Platform Recent Signals

### Hidden Rules: "平台不明示违规点" (strongest 2026-06 signal)

Across the highest-traffic official governance notes and creator videos sampled 2026-06-23, the single most common complaint is that creators are told they violated something but not *what or where*. Examples (see platform case files for ids): on Xiaohongshu's 交易导流 governance note, the top comment `麻烦平台把违规点写清楚呀，老提示违规，具体哪里违规又不明说` had ~2459 likes; Douyin appeal videos repeatedly show `申述时找不到违规作品，说作品一切正常`.

Review implication:

- Much enforcement runs on unwritten/隐形 rules. When a creator says "I don't know what I did wrong", do not conclude there is no violation — systematically audit the full public surface (caption, every image/OCR, cover, first frame, comments, pinned comment, profile, private-message prompt, product link) for the most likely category, especially 导流/营销/搬运.
- Conversely, low traffic with no notice is not proof of a violation; mark `待核验: 账号/作品状态`.
- This pattern is why creator-posted experience and comment discussion are kept as a valuable supplement: they map the practical edges of rules the official docs leave vague.

### AI and Synthetic Content

Regulator signal: the Central Cyberspace Affairs Commission Office reported the first stage of the 2025 `清朗·整治AI技术滥用` campaign on 2025-06-20. The campaign focused on AI face/voice misuse, missing labels for AI content, misleading synthetic content, illegal AI-product marketing, and platform detection obligations.

Review implication:

- Treat realistic AI face, voice, accident, disaster, public-affairs, celebrity, medical, legal, financial, or product-proof content as at least `Medium` unless prominently labeled.
- Escalate to `High` or `Blocker` when AI is used for impersonation, rumor, pornography/lowbrow content, fraud, fake authority, or marketing deception.

Traceable sources:

- 中国网信网, "中央网信办深入开展'清朗·整治AI技术滥用'专项行动第一阶段工作", 2025-06-20: https://www.cac.gov.cn/2025-06/20/c_1752129980667315.htm
- 中国网信网清朗专题 index, checked 2026-06-20: https://www.cac.gov.cn/wxzw/qinglang/A093711index_1.htm

### Short-Video Malicious Marketing

Regulator signal: the short-video malicious-marketing campaign targeted fake tragic personas, staged poverty/sadness, false information, public-order/morality violations, and off-platform diversion marketing. This campaign started before the primary window, but the pattern remains relevant and appears in 2025-2026 platform enforcement.

Review implication:

- Flag `卖惨`, fake identity/persona, fake public-interest story, pseudo-science, `专家/机构/内部消息` claims, and traffic-to-private-domain funnels together rather than as isolated wording issues.
- For platform-specific decisions, prefer newer platform rule pages or current official governance posts if they differ.

Traceable source:

- 中国网信网, "关于开展'清朗·整治短视频领域恶意营销乱象'专项行动的通知", 2025-04-15: https://www.cac.gov.cn/2025-04/15/c_1746334850258390.htm

### Staged / False Content → Real-World Legal Penalty

Signal (2026-06 sample): a Douyin `#抖音辟谣` news post (陕视新闻) reported that two people who staged/faked 高考-related stories to chase traffic were given administrative detention (10 and 5 days) by 西安 police. Comments confirm the pattern is endemic (`网上一搜全是开锁送准考证`; `行政拘留留案底，以后政审`).

Review implication:

- 摆拍/编造/蹭热点 around exams, accidents, charity, illness, public events, or rescues is not just a 限流 risk — it can be 治安处罚/行政拘留 and 造谣 liability. Escalate to `High`/`Blocker` and require real provenance.
- Do not present staged scenes as real; if dramatized, label clearly.

### E-commerce / 带货 Enforcement (fines, freezes, function bans)

Signal (2026-06 samples, Douyin): concrete creator-reported penalties include 抖店 fines (e.g. 自制食品无证被罚3万并停业), 罚款5000 + 永久关闭小黄车/商品分享 for directing viewers off-shop during live, and 货款冻结. Comment threads show 抖店/代运营 traps are common.

Review implication:

- For 带货/小店 content, verify product/食品/类目 qualification, link/price/gift consistency, and that live scripts do not point viewers to other shops, off-platform pages, or private contact (a frequent 封车 trigger).
- Flag "代运营包开店/包出单/稳赚" promos as 夸大收益/fraud risk.

### Official Rule-Education Channels (authoritative, traceable)

Each platform runs official rule/governance accounts whose posts are the most trustworthy in-platform source and double as rule explainers. Prefer these over creator anecdotes:

- 小红书: `规则百科薯`, `薯管家`, `商业合规薯`, `健康薯`, `好生意薯` (see `cases/xiaohongshu.md` for a themed note catalog).
- 快手: `#小心违规` / `#手规矩课堂` rule-education series and `@快手卖货助手`商家教育 (see `cases/kuaishou.md`).
- B站: `哔哩哔哩UP主服务中心` (e.g. the official限流-handling feature post; see `cases/bilibili.md`).

Caveat: even official posts often do not state the *specific* violation point (see "Hidden Rules" above), so still audit the full public surface.

## Cross-Platform Review Checklist Added From Cases

When auditing a self-media package, add these case-informed checks:

- Does the content pose as a normal user's authentic experience while hiding a commercial relationship?
- Are title, cover, comments, or private-message prompts creating a purchase funnel that the main video/article does not disclose?
- Are comments scripted, repetitive, self-question/self-answer, or coordinated across accounts?
- Does the content involve minors in any sexualized, unsafe, privacy-exposing, dating, self-harm, violent, or commercial context?
- Is AI or synthetic material realistic enough to mislead, and is it prominently labeled?
- Does the creator ask for likes, comments, shares, follows, `停留`, `互看`, or other engagement manipulation?
- If the issue is `限流/不收录/小眼睛为0/减少推荐`, is there actual platform notice evidence, or only an inferred traffic symptom?
- If advising an appeal, are the facts specific and evidence-backed rather than copied spam text?
- If the account claims `被盗/安全风险/异常登录`, is there login-device, IP/location, password-reset, operator-change, or third-party-tool evidence?
- If comments mention `代申诉/解封/封号/禁播/互举/内部看号`, is there grey-service, malicious-reporting, fraud, or diversion risk?
