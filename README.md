<div align="center">

# self-media-compliance-review

**自媒体视频发布前的违规风险审核 Skill。**

适用于 Claude Code / Codex / OpenClaw / Hermes 等支持 Skills 的 agent。把它装进 agent 后，可以在短视频、切片、封面、标题、字幕、口播、商品链接和发布文案交付前，让 AI 按平台规则做一遍结构化风险审核。

它不是“敏感词表”，而是一套面向发布前质检的审核流程：会检查画面、声音、文字、封面、评论引导、带货信息、资质、授权、引流和平台特有红线，并给出可执行的修改建议。

[![GitHub stars](https://img.shields.io/github/stars/JuneYaooo/self-media-compliance-review?style=flat)](https://github.com/JuneYaooo/self-media-compliance-review/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-black.svg)](./skills/self-media-compliance-review/SKILL.md)
[![Platforms](https://img.shields.io/badge/platforms-视频号%20%7C%20抖音%20%7C%20B站%20%7C%20小红书-orange.svg)](#-已覆盖平台)

</div>

---

## ✨ 能做什么

- 🧭 **多平台规则路由** — 根据目标平台自动读取视频号、抖音、B站、小红书的参考规则
- 🎬 **全发布面审核** — 不只审脚本，也审封面、标题、字幕、口播、画面、BGM、评论、商品链接和账号资料
- 🚦 **风险分级** — 输出 `Pass` / `Low` / `Medium` / `High` / `Blocker`
- 🔎 **证据定位** — 要求标注视频时间点、字幕行、封面文案、商品链接或待核验证据
- 🛠 **修改建议** — 给出消音、打码、删改、补资质、补授权、改写话术、移除链接等具体动作
- 📚 **可扩展规则库** — 新平台只需要新增一个 `references/<platform>.md`

## ✅ 适合哪些场景

| 场景 | 适合程度 | 说明 |
| --- | --- | --- |
| 短视频最终交付前审核 | 很适合 | 检查标题、封面、字幕、口播、画面和平台文案。 |
| 爆款切片 / B站切片 / 抖音切片 | 很适合 | 可接在剪辑和包装之后，作为发布前门禁。 |
| 带货视频风险检查 | 很适合 | 重点看商品链接、价格赠品一致性、虚假营销、引流和资质。 |
| 健康、财经、法律等高风险内容 | 适合 | 会标出资质、功效承诺、专业建议和误导风险。 |
| 版权、肖像、隐私复查 | 适合 | 会把授权、来源、肖像和隐私作为待核验项。 |
| 替代人工法务审核 | 不适合 | 本项目是风险控制辅助，不提供法律结论。 |

## 📱 已覆盖平台

| 平台 | 规则文件 |
| --- | --- |
| 微信视频号 / WeChat Channels | [`wechat-channels.md`](./skills/self-media-compliance-review/references/wechat-channels.md) |
| 抖音 / Douyin | [`douyin.md`](./skills/self-media-compliance-review/references/douyin.md) |
| B站 / Bilibili | [`bilibili.md`](./skills/self-media-compliance-review/references/bilibili.md) |
| 小红书 / Xiaohongshu | [`xiaohongshu.md`](./skills/self-media-compliance-review/references/xiaohongshu.md) |

规则来源汇总见：[`docs/sources.md`](./docs/sources.md)。

## 🚀 安装

### 方式一：让 AI 自己装（推荐）

把下面这段 prompt 丢给你的 AI 助手：

```text
帮我安装 self-media-compliance-review：
https://github.com/JuneYaooo/self-media-compliance-review
```

让 agent clone 仓库，并把 `skills/self-media-compliance-review/` 同步到当前运行环境的 skills 目录。

### 方式二：手动安装

```bash
git clone git@github.com:JuneYaooo/self-media-compliance-review.git
cd self-media-compliance-review

mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
rsync -a --delete skills/self-media-compliance-review/ \
  "${CODEX_HOME:-$HOME/.codex}/skills/self-media-compliance-review/"
```

安装后重启或刷新你的 agent session。

## 🛠 怎么用

直接用自然语言调用：

```text
使用 self-media-compliance-review，审核这个视频的标题、封面、字幕、口播、商品链接和发布文案，目标平台是抖音和小红书。
```

或在视频交付前：

```text
交付前跑一遍 self-media-compliance-review，平台是视频号、B站。
```

建议提供：

- 最终视频路径或可访问链接
- 口播稿、字幕、封面文案、标题、简介、评论区引导
- 商品链接、价格、赠品、活动规则
- 账号身份、资质证明、素材授权说明
- 目标平台和发布场景

## 📋 输出格式

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

## 🧪 校验

```bash
./scripts/validate.sh
```

校验内容包括：

- skill frontmatter 是否合法
- 平台参考文件是否齐全
- `SKILL.md` 是否挂载平台规则
- `docs/sources.md` 是否记录来源
- 是否残留 TODO / placeholder

## 🧩 项目结构

```text
skills/self-media-compliance-review/
  SKILL.md
  agents/openai.yaml
  references/
    wechat-channels.md
    douyin.md
    bilibili.md
    xiaohongshu.md

docs/
  sources.md

scripts/
  validate.sh
```

## ➕ 添加新平台

1. 新增 `skills/self-media-compliance-review/references/<platform>.md`
2. 在 `skills/self-media-compliance-review/SKILL.md` 的 Platform References 中挂载
3. 在 `docs/sources.md` 记录官方来源链接和抓取限制
4. 运行 `./scripts/validate.sh`

## ⚠️ 免责声明

本项目是发布前风险控制辅助工具，不是法律意见，也不能保证平台审核一定通过。平台规则、执法尺度和账号状态会变化，高风险内容发布前应重新核对官方规则，并由负责人做最终判断。

## License

MIT，详见 [LICENSE](./LICENSE)。
