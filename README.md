<div align="center">

# self-media-compliance-review

**自媒体视频发布前的违规风险审核 Skill。**

适用于 Claude Code / Codex / OpenClaw / Hermes 等支持 Skills 的 agent。把它装进 agent 后，可以在短视频、切片、封面、标题、字幕、口播、商品链接和发布文案交付前，按本仓库整理的参考规则做一遍结构化风险审核。

它不是“敏感词表”，而是一套面向发布前质检的审核流程：会检查画面、声音、文字、封面、评论引导、带货信息、资质、授权、引流和平台常见风险，并给出具体修改建议。

也欢迎大家在 [Issues](https://github.com/JuneYaooo/self-media-compliance-review/issues) 里提供各平台规则资料、审核经验、踩坑案例和整改思路。后续会不定期整理进这个 skill。

[![GitHub stars](https://img.shields.io/github/stars/JuneYaooo/self-media-compliance-review?style=flat)](https://github.com/JuneYaooo/self-media-compliance-review/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-black.svg)](./skills/self-media-compliance-review/SKILL.md)
[![Platforms](https://img.shields.io/badge/platforms-6%20platforms-orange.svg)](#-已覆盖平台)

</div>

---

## 能做什么

- **按平台读取参考文件**：根据目标平台读取视频号、微信公众号、抖音、快手、B站、小红书的规则参考。
- **覆盖常见发布面**：检查脚本、封面、标题、字幕、口播、画面、BGM、评论、商品链接和账号资料。
- **风险分级**：输出 `Pass` / `Low` / `Medium` / `High` / `Blocker`。
- **证据定位**：要求标注视频时间点、字幕行、封面文案、商品链接或待核验证据。
- **修改建议**：给出消音、打码、删改、补资质、补授权、改写话术、移除链接等具体动作。
- **案例排查参考**：对限流、封号、申诉、原创争议、评论灰产等场景给出排查方向和申诉材料清单。
- **可扩展规则文件**：新增平台时，可以按相同结构补充参考文件。

## 适合哪些场景

| 场景 | 适合程度 | 说明 |
| --- | --- | --- |
| 短视频最终交付前审核 | 适合 | 检查标题、封面、字幕、口播、画面和平台文案。 |
| 视频切片 / B站切片 / 抖音切片 | 适合 | 可接在剪辑和包装之后，作为发布前检查。 |
| 带货视频风险检查 | 适合 | 重点看商品链接、价格赠品一致性、虚假营销、引流和资质。 |
| 健康、财经、法律等高风险内容 | 适合 | 会标出资质、功效承诺、专业建议和误导风险。 |
| 版权、肖像、隐私复查 | 适合 | 会把授权、来源、肖像和隐私作为待核验项。 |
| 替代人工法务审核 | 不适合 | 本项目是风险控制辅助，不提供法律结论。 |

## 已覆盖平台

| 平台 | 规则文件 | 案例/申诉场景 |
| --- | --- | --- |
| 微信视频号 / WeChat Channels | [`wechat-channels.md`](./skills/self-media-compliance-review/references/wechat-channels.md) | [`cases/wechat-channels.md`](./skills/self-media-compliance-review/references/cases/wechat-channels.md) |
| 微信公众号 / WeChat Official Accounts | [`wechat-official-account.md`](./skills/self-media-compliance-review/references/wechat-official-account.md) | [`cases/wechat-official-account.md`](./skills/self-media-compliance-review/references/cases/wechat-official-account.md) |
| 抖音 / Douyin | [`douyin.md`](./skills/self-media-compliance-review/references/douyin.md) | [`cases/douyin.md`](./skills/self-media-compliance-review/references/cases/douyin.md) |
| 快手 / Kuaishou | [`kuaishou.md`](./skills/self-media-compliance-review/references/kuaishou.md) | [`cases/kuaishou.md`](./skills/self-media-compliance-review/references/cases/kuaishou.md) |
| B站 / Bilibili | [`bilibili.md`](./skills/self-media-compliance-review/references/bilibili.md) | [`cases/bilibili.md`](./skills/self-media-compliance-review/references/cases/bilibili.md) |
| 小红书 / Xiaohongshu | [`xiaohongshu.md`](./skills/self-media-compliance-review/references/xiaohongshu.md) | [`cases/xiaohongshu.md`](./skills/self-media-compliance-review/references/cases/xiaohongshu.md) |

规则来源汇总见：[`docs/sources.md`](./docs/sources.md)。跨平台案例索引见：[`recent-cases-2025-2026.md`](./skills/self-media-compliance-review/references/recent-cases-2025-2026.md)。

## 安装

把下面这段话发给你的 AI 助手即可：

```text
帮我安装 self-media-compliance-review：
https://github.com/JuneYaooo/self-media-compliance-review
```

安装方式取决于你正在使用的 agent。安装完成后，让它告诉你如何调用，以及是否需要重启或刷新当前 session。

## 怎么用

直接用自然语言调用：

```text
使用 self-media-compliance-review，审核这个视频的标题、封面、字幕、口播、商品链接和发布文案，目标平台是抖音和小红书。
```

或在视频交付前：

```text
交付前跑一遍 self-media-compliance-review，平台是视频号、B站。
```

排查账号状态或申诉问题：

```text
使用 self-media-compliance-review，帮我排查小红书笔记小眼睛为 0 的可能原因，并按案例库给出申诉前要准备的证据。
```

建议提供：

- 最终视频路径或可访问链接
- 口播稿、字幕、封面文案、标题、简介、评论区引导
- 商品链接、价格、赠品、活动规则
- 账号身份、资质证明、素材授权说明
- 目标平台和发布场景

## 输出格式

审核报告会尽量按这个结构输出：

```markdown
# 合规风险审核

- 平台: 抖音 / 小红书
- 内容范围: 视频、封面、标题、字幕、商品链接、发布文案
- 结论: High
- 最高风险: 标题和口播存在无法核验的功效承诺

## 风险明细

| 等级 | 平台/条款 | 证据位置 | 风险说明 | 修改建议 |
| --- | --- | --- | --- | --- |
| High | 小红书 商业推广/虚假营销 | 口播 00:12 | 暗示产品有确定功效 | 删除确定性承诺，改成体验描述并补证 |

## 待核验

- 产品资质
- 素材授权
- 商品链接价格和赠品是否一致
```

## 添加新平台

欢迎直接提 [Issue](https://github.com/JuneYaooo/self-media-compliance-review/issues) 或 PR。适合提供的信息包括：平台官方规则链接、实际违规提示截图、申诉经验、容易误判的内容类型、有效的整改方式。

## 致谢

- [LINUX DO](https://linux.do/)：中文开发者社区，感谢社区里关于 AI agent、Skills、自媒体工作流和内容生产实践的讨论。

## 免责声明

本项目是发布前风险控制辅助工具，不是法律意见，也不能保证平台审核一定通过。平台规则、执法尺度和账号状态会变化，高风险内容发布前应重新核对官方规则，并由负责人做最终判断。

## License

MIT，详见 [LICENSE](./LICENSE)。
