# Rule Sources

Last source audit: 2026-06-20.

Recent case audit: 2026-06-20.

Use official platform pages as the primary basis. If an official page is JavaScript-rendered or difficult to crawl, record that limitation in the platform reference file and prefer conservative review decisions.

## WeChat Channels

- 视频号常见违规内容概览: user-provided official text in the initial collection request.
- 微信视频号运营规范: referenced by the platform material; recheck the official page for high-stakes releases.
- Xiaohongshu discussion search samples for `视频号 违规 限流 封号 虚假营销` and `视频号 封号 申诉 怎么办`, 2026-06-20: see `references/cases/wechat-channels.md`.

## WeChat Official Accounts

- 微信公众平台运营规范: https://mp.weixin.qq.com/mp/opshowpage?action=newoplaw
- 微信公众平台服务协议: https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=1503979103&version=1&lang=zh_CN&platform=2
- 微信公众平台规则中心: https://mp.weixin.qq.com/webpoc/ruleCenter?type=oa
- 微信公众号和服务号推荐运营规范: https://mp.weixin.qq.com/cgi-bin/announce?action=getannouncement&key=11697600328G0Tbo&version=1&lang=zh_CN&platform=2
- Xiaohongshu discussion search samples for `微信公众号 封号 申诉 怎么办`, 2026-06-20: see `references/cases/wechat-official-account.md`.

Notes: the operation-norm page embeds rule text in `cgiData.content`; the service-agreement announcement page embeds content in page script. The local reference summarizes official categories and appeal evidence requirements without copying the full official text.

## Douyin

- 抖音规则中心: https://www.douyin.com/rule/policy
- 抖音用户服务协议: https://www.douyin.com/agreements/?id=6773906068725565448
- 抖音安全与信任中心: https://95152.douyin.com/
- 新浪财经转载综合报道 "小红书、抖音公告：永久封禁", 2026-06-06: https://finance.sina.com.cn/wm/2026-06-06/doc-inianuve1626360.shtml
- Xiaohongshu discussion search samples for `抖音 违规 封号 申诉 怎么办`, 2026-06-20: see `references/cases/douyin.md`.

Notes: the rule center is JavaScript-rendered. The current reference combines official rule-center routing with directly accessible user-service-agreement obligations.

## Kuaishou

- 快手社区管理规范: https://www.kuaishou.com/norm
- 快手直播管理规范: https://www.kuaishou.com/norm?tab=live
- 快手社区评论规范: https://www.kuaishou.com/norm?tab=comment
- 快手用户资料规范: https://www.kuaishou.com/norm?tab=userInfo
- 快手直播封面规范: https://www.kuaishou.com/norm?tab=liveCover
- 帐号违规被封禁了，怎么申诉解封？: https://www.kuaishou.com/help/feedback/2664?categoryId=hot
- 违法和不良信息举报受理和处置管理办法: https://www.kuaishou.com/help/report
- 快手软件许可及服务协议: https://www.kuaishou.com/about/policy
- Xiaohongshu discussion search samples for `快手 违规 封号 申诉 怎么办`, 2026-06-20: see `references/cases/kuaishou.md`.

## Bilibili

- bilibili社区公约: https://member.bilibili.com/studio/convention/content?index=3-1&navhide=1
- 社区规则 / 小黑屋入口: https://www.bilibili.com/blackboard/blackroom.html
- 小黑屋处罚条例V2.0: https://www.bilibili.com/blackboard/blackroomrule_v17.html
- 哔哩哔哩协议汇总: https://www.bilibili.com/blackboard/topic/activity-cn8bxPLzz.html
- 侵权申诉入口: https://www.bilibili.com/v/copyright/intro/
- Xiaohongshu discussion search samples for `B站 违规 小黑屋 申诉 怎么办` and `B站 小黑屋 处罚 公告 违规账号`, 2026-06-20: see `references/cases/bilibili.md`.

Notes: the community convention is JavaScript-rendered, but static bundle text exposes the detailed rule categories used in the reference.

## Xiaohongshu

- 小红书用户服务协议: https://agree.xiaohongshu.com/h5/terms/ZXXY20220331001/-1
- 品牌号社区运营规范 PDF: https://dc.xhscdn.com/file/c947aa537be9e80d802226374b5c710f/%E5%93%81%E7%89%8C%E5%8F%B7%E7%A4%BE%E5%8C%BA%E8%BF%90%E8%90%A5%E8%A7%84%E8%8C%83.pdf
- 小红书帮助中心: https://ad.xiaohongshu.com/help/docs
- 小红书蒲公英平台: https://pgy.xiaohongshu.com/help/home
- Community Covenant 2.0 public report: https://cn.chinadaily.com.cn/a/202601/20/WS696eef27a310942cc499bf9f.html
- Xiaohongshu false-marketing governance report: https://cn.chinadaily.com.cn/a/202509/18/WS68cbc60ba310f07257749344.html
- Xiaohongshu false-marketing governance report: https://economy.gmw.cn/2025-09/18/content_38294251.htm
- Xiaohongshu false-marketing governance report: https://www.stcn.com/article/detail/3344326.html
- Xiaohongshu minor-safety governance report, 2026-04-24: https://xinwen.bjd.com.cn/content/s69eb7573e4b0cd719ea1147e.html
- Xiaohongshu minor-safety governance report, 2026-06-01: https://newscdn.hndnews.com/hb/html/mobile/748349.html
- Xiaohongshu search/comment samples for `账号限流 怎么办`, `笔记违规 申诉`, and `薯管家 涉未成年人不良内容`, 2026-06-20: see `references/cases/xiaohongshu.md`.

Notes: Community Covenant 2.0 is used as directional context for 真诚分享, 友好互动, 有序经营. Detailed checks lean on the user agreement and brand-account operation rules.

## Optional Live Evidence

- TikHub Xiaohongshu search/comment tools, used only when `TIKHUB_API_KEY` is configured:
  - `xiaohongshu_web_v3_fetch_search_notes`
  - `xiaohongshu_web_v2_fetch_note_comments`
  - `xiaohongshu_web_v2_fetch_sub_comments`

Live Xiaohongshu creator notes and comments are discussion samples. 评论区讨论不是平台规则; use them only as symptom and remediation clues.

## Cross-Platform Regulators

- 中国网信网清朗专题 index: https://www.cac.gov.cn/wxzw/qinglang/A093711index_1.htm
- 中央网信办 "清朗·整治AI技术滥用" 第一阶段工作, 2025-06-20: https://www.cac.gov.cn/2025-06/20/c_1752129980667315.htm
- 中央网信办 "清朗·整治短视频领域恶意营销乱象" notice, 2025-04-15: https://www.cac.gov.cn/2025-04/15/c_1746334850258390.htm
- Recent case index and cross-platform checklist: `references/recent-cases-2025-2026.md`.
