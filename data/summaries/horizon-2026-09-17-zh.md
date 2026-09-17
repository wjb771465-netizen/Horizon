# Horizon 每日速递 - 2026-09-17

> 从 130 条内容中筛选出 5 条重要资讯。

---

**科技新闻**
1. [Flock 安全摄像头存在硬编码凭证和明文存储漏洞](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 推出 AI 驱动的广告体验](#item-tech-news-2) ⭐️ 8.0/10
3. [OpenAI 发布模型错位报告框架](#item-tech-news-3) ⭐️ 8.0/10
4. [GoBench：在围棋游戏中评估大语言模型](#item-tech-news-4) ⭐️ 8.0/10

**财经新闻**
1. [美联储三年来首次加息，暗示今年可能再次加息](#item-finance-news-1) ⭐️ 9.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [Flock 安全摄像头存在硬编码凭证和明文存储漏洞](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

安全研究人员发现 Flock 安全摄像头存在严重安全漏洞，包括硬编码凭证和明文数据存储，暴露了物联网设备在安全实践方面的重大缺陷。攻击者可利用硬编码的 API 密钥获取存储在明文中的凭证，进而可能访问 Flock 的服务器。这些漏洞揭示了部署在公共空间的监控设备在威胁建模和密钥管理方面的不足，引发了关于隐私和系统完整性的严重担忧。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**「背景」** Flock Safety 是一家主要在美国部署自动车牌识别（ALPR）摄像头的公司，其设备常用于社区执法和公共安全监控。这些摄像头通常安装在户外公共场所，旨在捕捉车辆图像并上传数据至云端进行分析。了解该公司的设备部署环境及其在公共监控领域的角色，有助于理解为何此次发现的安全漏洞引发了关于物理安全和数据隐私的严重担忧。

**「社区讨论」** 社区评论普遍认为硬编码凭证是极度无能的表现，并指出 Flock 的漏洞披露政策（VDP）形同虚设，实际上禁止了任何实质性的安全研究。用户批评这种做法是产品经理为了缩短上市时间而表现出的懒惰，忽视了设备部署在不受保护的公共空间所带来的物理访问威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#iot`, `#vulnerability`, `#privacy`, `#hardware`

---

<a id="item-tech-news-2"></a>
### [OpenAI 推出 AI 驱动的广告体验](https://openai.com/index/reimagining-advertising-with-ai) ⭐️ 8.0/10

OpenAI 宣布推出全新的 AI 驱动广告体验，其中包括“赞助代理”以及面向营销人员的专用工具。此次更新还包含与 HubSpot 和 Shopify 的集成，旨在将 AI 技术深度融入营销工作流程。这些举措标志着 OpenAI 正式进入广告技术领域，利用 AI 代理重塑广告互动方式。通过整合主要商业平台，OpenAI 试图为营销人员提供更高效的自动化解决方案。

rss · OpenAI Blog · 9月16日 13:00

**「背景」** OpenAI 正在测试“赞助代理”，允许用户在点击 ChatGPT 中的广告后与企业赞助的代理进行对话。此外，OpenAI 还推出了帮助广告商构建和运行营销活动的 AI 工具，并将 ChatGPT 广告功能集成到 HubSpot 和 Shopify 等平台中。这些举措标志着 OpenAI 正在进入广告技术领域，旨在挑战 Google 和 Meta 等现有巨头。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/reimagining-advertising-with-ai/">Reimagining advertising with AI | OpenAI</a></li>
<li><a href="https://thenextweb.com/news/openai-chatgpt-sponsored-agents-ads-manager-hubspot-shopify">“A clearly labeled conversation”: OpenAI tests Sponsored Agents in ChatGPT</a></li>
<li><a href="https://insideai.news/news/ai-in-business/openai-sponsored-agents/12073/">OpenAI Tests Sponsored Agents and AI Ad Tools in ChatGPT</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Advertising`, `#AI Agents`, `#Marketing`, `#Integrations`

---

<a id="item-tech-news-3"></a>
### [OpenAI 发布模型错位报告框架](https://openai.com/index/model-misalignment-reporting-framework) ⭐️ 8.0/10

OpenAI 推出了一个用于追踪、调查和披露模型错位的框架，并发布了六份记录意外或令人担忧的模型行为的报告。该框架旨在系统化地识别和处理人工智能模型在实际应用中表现出的与预期目标不一致的情况。通过公开具体的案例研究，OpenAI 希望提高开发过程的透明度，并促进行业在 AI 安全和模型对齐方面的标准化。这一举措标志着领先 AI 组织在应对模型行为不可预测性挑战方面迈出了重要一步。

rss · OpenAI Blog · 9月16日 17:00

**「背景」** 模型对齐是指确保人工智能系统的行为与人类意图、价值观和安全标准保持一致的技术领域，旨在防止模型产生有害、欺骗性或意外的输出。随着大语言模型能力的提升，识别和缓解模型在特定场景下偏离预期行为的“错位”现象已成为 AI 安全研究的核心挑战。OpenAI 此次发布的框架旨在建立一套标准化的流程，用于追踪、调查和披露这些模型错位案例，以提升行业透明度并促进安全技术的改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/model-misalignment-reporting-framework/">Our framework for reporting model misalignment - OpenAI</a></li>
<li><a href="https://alignment.openai.com/misalignment-reports/">Misalignment Notices and Reports · OpenAI Alignment</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Model Alignment`, `#OpenAI`, `#AI Governance`, `#Machine Learning`

---

<a id="item-tech-news-4"></a>
### [GoBench：在围棋游戏中评估大语言模型](https://www.reddit.com/r/MachineLearning/comments/1wi68jg/gobench_evaluating_llms_on_the_game_of_go_r/) ⭐️ 8.0/10

GoBench 是一个新的基准测试，通过让大语言模型（LLM）在 9x9 围棋棋盘上对抗从随机到超人类水平的 KataGo 对手阶梯来评估其推理能力。该基准测试与 ARC-AGI 2 表现出极强的相关性（r=0.83），并且目前远未饱和，其中表现最好的 GPT-6 Astra max 仅达到 2500 Elo，远低于 KataGo 的 4400 Elo。如果在评估前给予两小时的准备时间并使用编码工具，Codex 配合 Astra 可以达到 3560 Elo。作者承诺在基准测试饱和之前持续更新排行榜。

reddit · r/MachineLearning · /u/Roland31415 · 9月16日 18:54

**「背景」** ARC-AGI（Abstraction and Reasoning Corpus）是一个用于测试人工智能通用推理能力的基准，而 KataGo 是一个基于深度学习的强大围棋引擎。GoBench 利用 9x9 围棋这一具有明确规则和复杂策略的环境，旨在衡量模型在无需特定领域训练情况下的逻辑推理和规划能力。

**标签**: `#LLM Evaluation`, `#GoBench`, `#Reasoning`, `#Benchmark`, `#AI Agents`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美联储三年来首次加息，暗示今年可能再次加息](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html) ⭐️ 9.0/10

美联储批准了三年多来的首次加息，将目标利率区间上调至 3.75%-4%，并暗示今年晚些时候可能再次加息以抑制通胀。联邦公开市场委员会以 12 票全票通过了此次 25 个基点的加息决定。

rss · CNBC Finance · 9月16日 21:07

**「背景」** 美联储此前维持利率不变，但近期油价飙升和中东紧张局势加剧了通胀压力，促使政策转向。主席 Kevin Warsh 指出，尽管劳动力市场强劲，但通胀率仍高于央行 2%的目标。

**标签**: `#Federal Reserve`, `#Monetary Policy`, `#Interest Rates`, `#Inflation`, `#FOMC`

---

