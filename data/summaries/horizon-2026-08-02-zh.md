# Horizon 每日速递 - 2026-08-02

> 从 103 条内容中筛选出 9 条重要资讯。

---

**科技新闻**
1. [KataGo 神经网络内部对称性研究](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI Astra 以低成本解决十个数学难题](#item-tech-news-2) ⭐️ 7.0/10

**财经新闻**
1. [高盛交易业务有望创纪录，股票交易收入飙升 72%](#item-finance-news-1) ⭐️ 8.0/10
2. [美国将 43 家中国企业列入 UFLPA 实体清单](#item-finance-news-2) ⭐️ 7.0/10

**时政综合**
1. [休达移民危机引发欧洲政治风暴](#item-world-news-1) ⭐️ 8.0/10
2. [世卫组织：刚果（金）埃博拉疫情为史上最严重](#item-world-news-2) ⭐️ 8.0/10
3. [西非多国收紧反同性恋法律，活动人士发出警告](#item-world-news-3) ⭐️ 8.0/10
4. [欧盟将于周二召开紧急内政部长会议应对休达移民危机](#item-world-news-4) ⭐️ 8.0/10
5. [莫斯科餐厅爆炸致 3 死 21 伤](#item-world-news-5) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [KataGo 神经网络内部对称性研究](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 8.0/10

KataGo 作者发布了一项神经网络可解释性研究，分析开源围棋程序 KataGo 的神经网络如何内在表示棋盘对称性。围棋规则在旋转和反射下完全对称，但模型并未强制这种对称性，仅通过训练时随机 8 倍数据增强来随机化每个批次的空间方向。研究探讨了超人类水平的围棋神经网络是自动学习与方向无关的“对称”概念，还是需要逐方向分别记忆。文章主要由 AI 辅助撰写，但包含详细的人类指导和反馈，并附有代码链接，其中一项发现出乎意料。

reddit · r/MachineLearning · /u/icosaplex · 8月1日 16:18

**「背景」** KataGo 是一个开源的围棋引擎，采用类似 AlphaZero 的自我对弈强化学习方式从头训练，能够达到顶尖棋力，并支持多种棋盘尺寸和规则。围棋规则在旋转和翻转下完全对称，但 KataGo 的神经网络并未在结构上强制这种对称性，仅通过训练时的随机八重数据增强（随机化每个批次的空间朝向）来隐含地处理对称性。这篇研究正是围绕这种未强制的对称性，探讨超强围棋网络内部是否自动学会了与朝向无关的表征。

**「影响」** 这项关于 KataGo 的研究为游戏 AI 开发者和可解释性研究者提供了具体证据：即使不强制对称性，仅靠训练时的 8 倍随机方向数据增强，超人类水平的围棋神经网络也能部分学会与棋盘方向无关的内部表征，但并非完全如此，仍存在依赖方向的表征。这意味着在类似对对称性敏感的任务中，数据增强无法完全替代架构上的不变性设计，KataGo 的维护者和使用者应继续保留增强策略，同时可依据该发现探索更有效的对称性利用方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lightvector/KataGo">GitHub - lightvector/KataGo: GTP engine and self-play ...</a></li>
<li><a href="https://katagotraining.org/">KataGo Distributed Training</a></li>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo - Wikipedia</a></li>

</ul>
</details>

**标签**: `#neural network interpretability`, `#Go`, `#symmetry`, `#KataGo`, `#machine learning`

---

<a id="item-tech-news-2"></a>
### [OpenAI Astra 以低成本解决十个数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 7.0/10

OpenAI 宣布，其下一代主力模型 Astra 的一个内部版本以每个问题不到 2,000 美元（按 GPT-5.6 Sol 代币价格计算）的成本，解决了十个至少十年未有主要进展的数学问题。OpenAI 在 GitHub 的 openai/ten-proofs 仓库提供了 Lean 4 形式化证明，并发布了描述解法的论文以及一份由模型根据未公开推理轨迹重建证明过程的 PDF。Simon Willison 指出，OpenAI 没有公布在未解问题上花费的金额，也未公开所使用的提示词，因此透明度仍有限；此前 Anthropic 曾用 Claude 和 Mythos Preview 在花费 10 万代币成本后发现密码学弱点。数学家群体对此反应强烈，有人称之为“深蓝时刻”，Terence Tao 则将其与“大数学”的愿景联系起来。

rss · Simon Willison · 8月1日 20:34

**「背景」** OpenAI 宣布其下一代模型 Astra 的内部版本以极低成本解决了数学和理论计算机科学中的十个长期未解问题，这些问题的主要结果至少十年没有进展。Lean 4 是一种交互式定理证明器，常用于将数学证明形式化并验证其正确性；OpenAI 在 GitHub 仓库中提供了其结果的 Lean 4 形式化证明。近年来，人工智能模型越来越多地被用于数学研究，例如 Anthropic 的 Claude 也曾被用于发现密码学弱点，而此次 OpenAI 的成果被视为 AI 辅助数学研究的又一进展。

**「影响」** 如果这些结果经独立验证属实，Astra 将显著降低数学研究的计算成本，并可能加速形式化证明和“大数学”式人机协作；但由于缺少失败尝试数据，实际成功率尚不明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/ten-advances-in-mathematics/">Ten advances in mathematics and theoretical computer ... | OpenAI</a></li>
<li><a href="https://digg.com/tech/9qjs9782">OpenAI Astra Model Solves Ten Open Problems · Digg</a></li>
<li><a href="https://gizmodo.com/openai-smuggled-the-announcement-of-astra-its-next-ai-model-into-a-blog-post-about-math-2000793689">OpenAI Smuggled the Announcement of Astra , Its Next AI Model, Into...</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#theoretical computer science`, `#research`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [高盛交易业务有望创纪录，股票交易收入飙升 72%](https://www.cnbc.com/2026/08/01/goldman-traders-are-on-pace-for-a-record-year-a-close-up-look-at-how-theyre-doing-it.html) ⭐️ 8.0/10

高盛第二季度股票交易收入跃升 72%，达到创纪录的 74.2 亿美元（实际业绩），推动交易业务有望创下年度新高。同期投行收入增长 55%至 34 亿美元，固定收益、外汇及大宗商品（FICC）收入增长 32%至 46 亿美元。

rss · CNBC Finance · 8月1日 20:22

**「背景」** 增长来自高盛多年投入和跨部门客户协同，同时受益于市场波动、企业并购与 IPO 活跃，以及 AI 资本开支周期带来的交易需求。

**标签**: `#Goldman Sachs`, `#trading revenue`, `#equities`, `#investment banking`, `#earnings`

---

<a id="item-finance-news-2"></a>
### [美国将 43 家中国企业列入 UFLPA 实体清单](https://companies.caixin.com/2026-08-01/102470547.html) ⭐️ 7.0/10

当地时间 7 月 31 日，美国国土安全部宣布将 43 家中国企业列入 UFLPA 实体清单，新增名单于 8 月 3 日生效，涉及福建七匹狼、洽洽食品、思念食品等企业。

telegram · zaihuapd · 8月2日 05:23

**「背景」** UFLPA 即《维吾尔强迫劳动预防法》，美国国土安全部依据该法设立“实体清单”，列入清单的企业所生产的商品将被推定涉及强迫劳动并禁止进入美国市场。此次新增的 43 家企业中有约一半位于新疆以外，清单于 2026 年 8 月 3 日生效。

**「影响」** 从 2026 年 8 月 3 日起，七匹狼、洽洽食品、思念食品等入列企业全部或部分参与生产的商品在进入美国时受“强迫劳动”推定约束，美国海关可拒绝放行，除非企业能举证未使用强迫劳动，相关对美出口面临中断或审查风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kharon.com/resources/article/forced-labor/dhs-uflpa-entity-list-additions">DHS Added 43 Chinese Firms to the UFLPA Entity List. Kharon ...</a></li>
<li><a href="https://www.dhs.gov/news/2026/07/31/dhs-announces-addition-43-companies-uflpa-entity-list">DHS Announces the Addition of 43 Companies to the UFLPA ...</a></li>
<li><a href="https://www.dhs.gov/uflpa-entity-list">UFLPA Entity List - Homeland Security</a></li>
<li><a href="https://www.kharon.com/resources/article/forced-labor/dhs-uflpa-entity-list-additions">DHS Added 43 Chinese Firms to the UFLPA Entity List. Kharon Flagged 41 Long Before the Listing.</a></li>
<li><a href="https://www.kelleydrye.com/viewpoints/blogs/trade-and-manufacturing-monitor/u-s-government-announces-largest-expansion-of-the-uflpa-entity-list-in-history-continues-focus-on-forced-labor-trade-enforcement">U.S. Government Announces Largest Expansion of the UFLPA Entity List…</a></li>
<li><a href="https://2paragraphs.com/2026/08/markwayne-mullins-ban-of-43-chinese-companies-includes-snacks-and-shirts/">Markwayne Mullin’s Ban of 43 Chinese Companies Includes Snacks and Shirts</a></li>

</ul>
</details>

**标签**: `#UFLPA`, `#China`, `#entity list`, `#trade policy`, `#sanctions`

---

## 时政综合

<a id="item-world-news-1"></a>
### [休达移民危机引发欧洲政治风暴](https://www.bbc.co.uk/news/articles/c62vl925dqdo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 8.0/10

大量移民从摩洛哥进入西班牙北非飞地休达，西班牙官员称大部分已返回，但事件在社交媒体炒作下引发欧洲政治风暴，暴露出欧盟在移民政策上的分歧。

rss · BBC World · 8月2日 00:55

**「背景」** 休达是西班牙位于北非海岸的飞地，与摩洛哥接壤。据报有近 6 万名移民在约 24 小时内从摩洛哥涌入休达，使当地人口增加约七成，触发外交风波并暴露欧洲在移民政策上的分歧。

**「影响」** 该事件冲击欧洲政坛，使欧盟在移民政策上的分歧公开化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rtrunews.com/news/643727-spain-ceuta-crisis-explainer/">Why did nearly 60,000 migrants suddenly storm the border into Spain ?</a></li>

</ul>
</details>

**标签**: `#migration`, `#Spain`, `#Ceuta`, `#European politics`, `#Morocco`

---

<a id="item-world-news-2"></a>
### [世卫组织：刚果（金）埃博拉疫情为史上最严重](https://www.bbc.co.uk/news/articles/cy07qe0knvzo?at_medium=RSS&amp;at_campaign=rss) ⭐️ 8.0/10

世界卫生组织表示，刚果民主共和国当前的埃博拉疫情是该国历史上最严重的一次，已导致 1587 人死亡，目前仍没有获批的疫苗或治疗方法。

rss · BBC World · 8月1日 16:16

**「背景」** 刚果（金）自 1976 年以来多次出现埃博拉疫情，本次是该国第 17 次疫情暴发，且距上一轮结束仅五个月。此次由本迪布焦型病毒引起，目前尚无获批疫苗或特效药。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Ebola_epidemic">2026 Ebola epidemic - Wikipedia</a></li>
<li><a href="https://www.bbc.com/news/articles/cy07qe0knvzo">Ebola Bundibugyo strain outbreak worst ever in DR Congo, WHO says</a></li>

</ul>
</details>

**标签**: `#Ebola`, `#DR Congo`, `#public health`, `#epidemic`, `#WHO`

---

<a id="item-world-news-3"></a>
### [西非多国收紧反同性恋法律，活动人士发出警告](https://www.theguardian.com/world/2026/aug/02/anti-lgbtq-laws-are-on-the-rise-across-west-africa-campaigners-warn) ⭐️ 8.0/10

活动人士警告，西非多国正在出台或加强反同性恋法律；塞内加尔今年 3 月将同性性行为的最高刑期加倍至 10 年，并将“宣扬”同性恋列为犯罪，尼日尔今年 2 月也首次将同性性关系定为犯罪。

rss · Guardian World · 8月2日 04:00

**「背景」** 西非多国近年加强针对同性恋群体的法律。2026 年 3 月，塞内加尔将同性性行为最高刑期加倍至 10 年，并新增对“宣扬”同性恋的处罚；同年 2 月，尼日尔首次将同性性关系定为犯罪。布基纳法索和马里也在 2024 至 2025 年新刑法中禁止同性关系。

**「影响」** 新法已在实际执法中产生后果：尼日尔通过新刑法后，当地倡导者称至少有 40 人被捕、16 人入狱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/world/2026/aug/02/anti-lgbtq-laws-are-on-the-rise-across-west-africa-campaigners-warn">Anti-LGBTQ+ laws are on the rise across west Africa ...</a></li>
<li><a href="https://www.africanhrc.org/single-post/senegal-enactment-of-new-law-heightens-the-hunt-for-gays">Senegal Anti-LGBT Law 2026: Increased Arrests ...</a></li>
<li><a href="https://ket.brussels/2026/06/11/when-love-becomes-a-crime-nigers-new-anti-lgbt-law-and-what-it-means-for-our-communities/">When love becomes a crime: Niger’s new anti-LGBT law and what ...</a></li>
<li><a href="https://gomag.com/article/40-people-arrested-niger-after-new-anti-lgbtq-laws/">At Least 40 People Arrested in Niger After New Anti - LGBTQ+ Laws ...</a></li>

</ul>
</details>

**标签**: `#LGBTQ+ rights`, `#West Africa`, `#Senegal`, `#Niger`, `#human rights legislation`

---

<a id="item-world-news-4"></a>
### [欧盟将于周二召开紧急内政部长会议应对休达移民危机](https://www.theguardian.com/world/2026/aug/01/spain-pedro-sanchez-calls-for-eu-meeting-ceuta-border-crossing) ⭐️ 8.0/10

欧盟决定下周二召开内政部长紧急会议，此前超过 5 万名移民进入西班牙在北非的飞地休达。西班牙首相桑切斯呼吁欧盟采取行动，但成员国之间仍存在分歧。

rss · Guardian World · 8月1日 19:03

**「背景」** 休达（Ceuta）是西班牙位于摩洛哥海岸的飞地，也是欧盟外部边境；2026 年 7 月底超过 5 万名移民从摩洛哥涌入，促使西班牙要求欧盟召开紧急会议，但成员国在移民政策上分歧依旧。

**「影响」** 意大利已对西班牙恢复边境检查并暂时中止其在申根区的自由通行权，直接冲击双方航班、海运和人员流动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Morocco%E2%80%93Spain_border_incident">2026 Morocco–Spain border incident - Wikipedia</a></li>
<li><a href="https://dw.com/en/ceuta-spain-says-most-migrants-have-returned-to-morocco/live-78191601">Ceuta: Spain demands EU meeting, blasts &#x27;selfish&#x27; response</a></li>
<li><a href="https://thehill.com/policy/international/6003064-ceuta-migration-spain-morocco-italy/">Ceuta migrant crisis sparks EU border tensions</a></li>

</ul>
</details>

**标签**: `#EU migration crisis`, `#Ceuta`, `#border security`, `#Spanish foreign policy`, `#Frontex`

---

<a id="item-world-news-5"></a>
### [莫斯科餐厅爆炸致 3 死 21 伤](https://www.theguardian.com/world/2026/aug/02/moscow-restaurant-bombing-kills-three-people-as-device-carried-by-woman-explodes) ⭐️ 8.0/10

莫斯科警方称，一名女子携带的自制炸弹在市中心一家意大利餐厅附近发生爆炸，造成 3 人死亡、至少 21 人受伤。爆炸发生于周六晚 8 时前，地点为库德林斯卡亚广场一座斯大林时代高层建筑旁。

rss · Guardian World · 8月2日 00:22

**「背景」** 事发建筑是莫斯科七座斯大林式高层建筑之一，位于库德林斯卡亚广场。

**标签**: `#Moscow`, `#bombing`, `#Russia`, `#terrorism`, `#casualties`

---

