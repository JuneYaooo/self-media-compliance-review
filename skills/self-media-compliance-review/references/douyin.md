# Douyin Compliance Reference

Use this reference when the target platform is 抖音 / Douyin, 抖音极速版, 抖音火山版, or a China short-video package likely to be republished to Douyin.

Source audit date: 2026-06-19.

Primary sources:

- 抖音规则中心: https://www.douyin.com/rule/policy
- 抖音用户服务协议: https://www.douyin.com/agreements/?id=6773906068725565448
- 抖音安全与信任中心: https://95152.douyin.com/
- 抖音侵权投诉/申诉入口 referenced from the user service agreement.

Source note: the official rule center and trust center are JavaScript-rendered pages. The user service agreement provides stable, directly readable baseline obligations; platform-specific rule-center material should be rechecked in browser if a content decision is high-stakes.

## Severity Hints

- `Blocker`: illegal/prohibited content under information-content rules; porn, gambling, violent crime, terrorism/extremism, national-security risk, defamation/privacy/IP infringement, unauthorized impersonation, obvious unmarked AI/deepfake deception, dangerous challenge likely to cause injury/death, fraud/illegal ads, serious platform-security abuse.
- `High`: likely "不良内容" or platform-order risk: sexual implication, gore/horror, cyberbullying, exaggerated title mismatch, disaster sensationalism, minors imitating unsafe behavior, spam marketing, commercial solicitation, traffic diversion, unverified source for public affairs.
- `Medium`: context-dependent risk requiring source labels, AI labels, qualification, disclosure, rights proof, or safer wording.
- `Low`: mild wording, UX, cover/title, or evidence-retention issue.

## Core Douyin Checks

### 1. Account and Identity

Flag:

- Account nickname/avatar/bio/抖音号 impersonates a person, institution, brand, or public-known identity.
- Account information misleads the public about ownership or affiliation.
- Account is lent, rented, sold, transferred, or operated by a non-owner.
- Publishing, livestreaming, or messaging occurs without required registration or real-name authentication.

Evidence to request: account profile screenshot, certification status, business/entity authorization, delegated operation proof.

### 2. Illegal or Prohibited Information

Douyin user service agreement prohibits producing, copying, publishing, or spreading illegal content. Treat the following as hard red-line categories:

- Opposing constitutional basic principles.
- National security, state secrets, subversion, national unity or sovereignty risk.
- Damage to national honor/interests.
- Insulting, defaming, or distorting heroic martyrs.
- Terrorism, extremism, or inciting terrorist/extremist activity.
- Ethnic hatred/discrimination and undermining ethnic unity.
- Breaking national religious policy, cults, superstition.
- Rumors or false information that disturb economic/social order or stability.
- Obscenity, pornography, gambling, violence, murder, terror, or criminal instruction.
- Insults, defamation, or infringement of reputation, privacy, portrait, IP, or other rights.
- Commercial advertisements violating internet-advertising laws.
- Other legally forbidden content.

### 3. Bad Information and Community Atmosphere

Flag:

- Exaggerated titles where content and title seriously mismatch.
- Hype around scandals, gossip, misconduct, or disgrace.
- Inappropriate commentary on natural disasters, major accidents, casualties, or public crises.
- Sexual implication, sexual teasing, or phrasing that invites sexual association.
- Bloody, scary, cruel, or physically/psychologically disturbing content.
- Inciting crowd discrimination, regional discrimination, or other group hostility.
- Vulgar, kitsch, or lowbrow content.
- Content that may lead minors to imitate unsafe or immoral behavior or form bad habits.
- Violent intimidation, threats, or cyberbullying.
- Dirty language that damages public order and morals.

### 4. Dangerous Behavior

Flag content that contains high danger or harms performer/viewer health:

- Violence or self-harm.
- Life/health-threatening performances, dangerous equipment, dangerous methods, or property-safety hazards.
- Encouraging or inducing others to participate in dangerous activity that may cause injury or death.

Remediation: remove the sequence, add clear safety framing only when the action is legitimate and non-instructive, avoid challenge/教程/模仿 language, and do not use dangerous frames as cover/opening.

### 5. AI, Deep Synthesis, and Synthetic Media

Flag:

- AI/deep-learning/VR/generated content used to create rumors, misinformation, impersonation, or infringement.
- Non-realistic audio/video, AI face/voice, virtual scenes, or synthetic event footage without prominent labeling when users may confuse it with real events.
- Synthetic public-affairs, disaster, accident, celebrity, medical, financial, or legal content without source and label.

Required fix: add a clear public-facing AI/synthetic label; for sensitive events, avoid realistic fake footage unless editorially necessary and unmistakably labeled.

### 6. Platform Order and Spam Marketing

Flag:

- Spam information, commercial solicitation, excessive marketing.
- Comments unrelated to the content being commented on.
- Character combinations, homophones, cropped screenshots, watermarks, or other tricks used to evade review.
- Plugin, script, crawler, automation, bulk registration, fake data, or any behavior interfering with Douyin systems.
- Unauthorized scraping, copying, mirroring, re-uploading, deep links, modified Douyin identifiers, or use of Douyin information/content outside allowed contexts.

### 7. Advertising, Product, and Finance Risk

Flag:

- Commercial ads that do not meet advertising-law requirements.
- Oral/written guarantees made in ads or promotions without substantiation.
- Medical, finance, loan, investment, insurance, education, legal, and other high-impact fields presented as professional advice without verified qualifications.
- Financial links or recommendations, especially loans, investment, or wealth-management topics, without risk disclosure and qualification.
- Product effects, prices, gifts, activity limits, or before/after claims that are not verifiable or not aligned with the link.

For AI-generated advice, Douyin agreement explicitly warns that AI output is general information and cannot replace professional advice in medical, financial, legal, education, and similar fields. Treat professional-scenario AI advice as `High` unless clearly generalized and non-prescriptive.

### 8. Rights and Authorization

Flag:

- Content components are not original or legally authorized: video, image, text, music, sound, lines, visual design, dialogue, portrait, name, trademark, or brand asset.
- Unauthorized use of Douyin marks such as "抖音", "douyin.com", logos, domain names, or confusing brand identifiers.
- Defamation, privacy leak, unauthorized portrait, copyright, trademark, or other rights risk.
- Reposting, clipping, or commercial use of Douyin content outside permitted contexts.

Evidence to request: source file, license, platform download rights, music license, portrait authorization, trademark/brand permission.

### 9. Minors

Flag:

- Minors' portrait, voice, or personal information used without guardian/right-holder consent.
- Content exposing minor identity, school, address, whereabouts, or private life.
- Unsafe behavior, bad habits, cyberbullying, immoral behavior, or risky consumption involving minors.
- Minor-facing content that encourages addiction, unsafe meetups, insults/fraud, or harmful online behavior.

### 10. Report Labels

Use platform labels such as:

- `抖音 用户服务协议 4.2 违法违规内容`
- `抖音 用户服务协议 4.3 不良内容`
- `抖音 用户服务协议 4.4 高危险性内容`
- `抖音 用户服务协议 4.5 AI/深度合成标识`
- `抖音 用户服务协议 4.6 扰乱平台经营秩序`
- `抖音 用户服务协议 10.2 内容权利/原创授权`
- `抖音 用户服务协议 13 未成年人`

