# Horizon 每日速递 - 2026-08-14

> 从 135 条内容中筛选出 6 条重要资讯。

---

**科技新闻**
1. [DRAM 攻击工具 Spaghettifying DRAM 发布，针对 AMD 系统](#item-tech-news-1) ⭐️ 9.0/10
2. [DeepSeek V4 Pro 0813 发布：开放权重、仅 API 提供](#item-tech-news-2) ⭐️ 9.0/10
3. [Hugging Face 复现 2,200 篇 ICML 论文的经验教训](#item-tech-news-3) ⭐️ 8.0/10
4. [GPT-5.6 构建者指南：更快速、更具成本效益的 AI 智能体](#item-tech-news-4) ⭐️ 8.0/10
5. [DeepMind 发布手语转文字模型 SL2T，Pixel 11 首次搭载](#item-tech-news-5) ⭐️ 8.0/10

**时政综合**
1. [刚果（金）埃博拉疫情扩散至第六个省份](#item-world-news-1) ⭐️ 9.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [DRAM 攻击工具 Spaghettifying DRAM 发布，针对 AMD 系统](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

安全研究员发布了一款名为 Skitter Creek Bath Salts 的 DRAM 漏洞利用工具，可在 AMD 系统上实现内存破坏攻击，并配套有 Black Hat 大会演讲。该工具的 README 显示其主要在 AMD Jaguar（2013 年的低功耗架构）上验证，仅提及 Zen 3 的内存控制器寄存器基址不同，因此对更新 CPU 的实际影响仍不确定。这项工作突出了现代 DRAM 控制器作为攻击面的重要性，可能影响硬件安全研究和游戏机等封闭平台的安全评估。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**「背景」** 该工具名为 Skitter Creek Bath Salts，针对 AMD Family 16h（Jaguar 架构，约 2013 年）处理器的 DRAM 控制器，通过翻转一个配置位来重新映射物理地址，使研究者能够读写内存单元，而平台安全处理器（PSP）、系统管理模式（SMM）等保护机制仍基于旧的地址映射进行校验，从而被绕过。DRAM 地址加扰是处理器厂商用来混淆物理内存布局的机制，过去被认为是可信的硬件边界，这项研究展示了该机制可以被软件在 ring 0 权限下轻易破坏，进而访问通常被认为位于“负环”（negative ring）中受保护的系统资源。

**「影响」** 该工具让已在受影响的 AMD Jaguar（AMD16h）系统上获得 ring 0 代码执行权限的攻击者能够直接操作 DRAM 内存控制器寄存器，从而访问通常被隐藏的“负 ring”特权区域；不过 README 仅明确支持 2013 年的 Jaguar 架构，并提到 Zen 3 已改变内存控制器寄存器基地址，因此对当前主流 CPU 的实际影响仍不明确，需等待 Black Hat 演示进一步说明。

**「社区讨论」** 评论者期待 Christopher Domas 的 Black Hat 演讲，并称赞其以往在逆向工程等主题上的出色讲解能力。还有评论指出 DRAM 控制器如今复杂且依赖专有二进制组件，攻击面巨大；同时有人质疑该工具对较新 CPU 的实际影响，仅凭 README 中的 AMD Jaguar 信息不足以判断。另有观点认为，这类工具让用户获得对自己系统的完全底层访问权，但也可能让 Xbox 和 PlayStation 等平台的安全团队感到紧张。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/ skitter - creek - bath - salts : Unlocking...</a></li>
<li><a href="https://dzen.ru/b/an3nioa_N0hzeys8">Один бит в контроллере DRAM открывает всю память... | Дзен</a></li>

</ul>
</details>

**标签**: `#DRAM`, `#hardware security`, `#exploitation`, `#AMD`, `#Black Hat`

---

<a id="item-tech-news-2"></a>
### [DeepSeek V4 Pro 0813 发布：开放权重、仅 API 提供](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 9.0/10

DeepSeek V4 Pro 0813 已通过 API 发布，目前没有官方公告页面，但权重已上传至 Hugging Face，共 1.7T 参数、893 GB。作者 Simon Willison 在 OpenRouter 上体验后，发现低、中、高三种推理等级生成的“骑自行车鹈鹕”图像差异极大，这是他从未在其他模型上见过的现象。基准测试数据据称先发布在 DeepSeek 官方微信群，然后被贴到 Reddit 后被版主删除，最终以 ASCII 表格形式出现在 Hacker News 上。Telegram 消息补充称，DeepSeek-V4-Pro 正式版已同步上线 APP、网页端和 API，模型名为 deepseek-v4-pro，增强 Agent 能力、原生支持 Responses API 格式并适配 Codex。API 将实行峰谷定价，闲时价格为高峰时段一半，新价格于 2026 年 8 月 17 日 0 时生效。

rss · Simon Willison · 8月12日 23:59

**「背景」** DeepSeek 是中国 AI 实验室，其 V4 系列模型以开放权重形式发布，此前已有 4 月的 V4-Pro 和 7 月的 V4-Flash-0731。2026 年 8 月 13 日发布的 V4 Pro 0813 先通过 OpenRouter 等 API 上线，随后官方在 Hugging Face 放出开放权重，规格为 1.7T 参数、893 GB。该版本增强 Agent 能力，原生支持 Responses API 格式，并提供多种思考档位。

**「影响」** 使用 DeepSeek API 的开发者可直接调用 deepseek-v4-pro 模型，同时可下载 1.7T 参数的开源权重进行本地部署；峰谷定价生效后，闲时调用成本将降低一半。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813">deepseek-ai/DeepSeek-V4-Pro-0813 · Hugging Face</a></li>
<li><a href="https://aireleasetracker.com/model/deepseek/deepseek-v4-pro-0813">DeepSeek-V4-Pro-0813 — Benchmarks, Specs &amp; Release Date</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#AI`, `#language model`, `#open weights`, `#API`

---

<a id="item-tech-news-3"></a>
### [Hugging Face 复现 2,200 篇 ICML 论文的经验教训](https://huggingface.co/blog/icml-2026-open-reproductions) ⭐️ 8.0/10

Hugging Face 在一篇博客文章中总结了其大规模复现 2,200 篇 ICML 论文的经验，重点关注机器学习研究中的可复现性挑战。该工作揭示了当前论文在代码、数据和实验细节方面普遍存在的不足，并提出了改进研究实践的具体建议。这次大规模复现努力为社区提供了关于如何提升人工智能研究透明度和可验证性的重要参考。尽管具体的复现结果和案例细节尚未完全公开，但该博客本身已成为推动可复现性讨论的重要贡献。

rss · Hugging Face Blog · 8月13日 00:00

**「背景」** 2026 年 7 月 15 日至 8 月 2 日，Hugging Face 与社区共同发起了“ICML 2026 Agent Repro Challenge”黑客松，超过 1200 名社区成员使用各自的编码智能体，试图逐项复现 ICML 2026 论文的主要结论。在 19 天内，参与者发布了 6816 份 Trackio 日志，成功复现了 2226 篇论文，约占会议论文总数的三分之一；每项复现声明会由自动化评审员对照 Hugging Face Space 日志给出判定。该博客文章总结了这次大规模复现努力的经验教训，并探讨了智能体在研究实验中扮演的角色。

**「影响」** Hugging Face 通过复现 2,200 篇 ICML 论文，为机器学习社区提供了大规模可复现性挑战的实际证据；结合已有研究指出的数据/代码不公开、训练条件敏感等问题，这项工作的教训有助于推动研究者和会议在论文发表时更严格地要求开放数据和代码，并促进复现工具与最佳实践的采纳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/blog/blob/main/icml-2026-open-reproductions.md">blog/icml-2026-open-reproductions.md at main · huggingface ...</a></li>
<li><a href="https://prismix.dev/news/57f8b7f378e9">What We Learned by Reproducing 2,200 papers from ICML</a></li>
<li><a href="https://github.com/will-rice/icml-2026-reproductions/tree/main/">GitHub - will-rice/icml-2026-reproductions</a></li>
<li><a href="https://paperswithcode.co/paper/2307.10320">Reproducibility in Machine Learning -Driven Research ...</a></li>

</ul>
</details>

**标签**: `#reproducibility`, `#machine learning research`, `#ICML`, `#open source`, `#AI evaluation`

---

<a id="item-tech-news-4"></a>
### [GPT-5.6 构建者指南：更快速、更具成本效益的 AI 智能体](https://openai.com/index/builders-guide-to-gpt-5-6) ⭐️ 8.0/10

OpenAI 发布了针对 GPT-5.6 的构建者指南，重点介绍初创公司如何利用更智能的模型选择和改进的 Responses API 能力，构建更快、更具成本效益的 AI 智能体。该指南强调，开发者可以根据具体任务选择合适的模型，以平衡性能与成本。目前公开的摘要信息有限，未提供关于 GPT-5.6 新功能的更多技术细节。

rss · OpenAI Blog · 8月13日 11:00

**「背景」** GPT-5.6 是 OpenAI 发布的新一代模型系列，通过不同的模型变体（如 gpt-5.6-sol 面向前沿能力、gpt-5.6-terra 平衡智能与成本、gpt-5.6-luna 面向高效高吞吐场景）来满足多样化的应用需求，同时 gpt-5.6 别名默认路由到 gpt-5.6-sol。该系列主要配合 Responses API 使用，用于推理、工具调用和多轮对话等 AI 智能体工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/latest-model">Model guidance | OpenAI API</a></li>
<li><a href="https://developers.openai.com/api/docs">OpenAI API Platform Documentation</a></li>

</ul>
</details>

**标签**: `#gpt-5.6`, `#openai`, `#api`, `#ai-agents`, `#model-selection`

---

<a id="item-tech-news-5"></a>
### [DeepMind 发布手语转文字模型 SL2T，Pixel 11 首次搭载](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

谷歌 DeepMind 发布大规模多语言手语转文字模型 SL2T，并首次将其落地到消费产品中：Pixel 11 的 Gboard 键盘和 Live Transcribe 实时字幕现已支持美国手语转英语。该模型使用超过 10 万小时、覆盖 50 多种手语的数据训练，在 FLEURS-ASL 基准上的零样本得分为 70 BLEURT，显著高于此前的纪录。为保护隐私，模型只处理手部和身体姿态关键点，不读取原始视频。后续官方计划将支持扩展至更多设备和语言。

telegram · zaihuapd · 8月13日 08:55

**「背景」** 手语识别与翻译长期以来依赖特定词汇或有限场景的监督数据，难以覆盖真实世界中多样且连续的手语表达。SL2T 是大规模多语言手语转文字模型，通过海量多语言训练数据实现零样本泛化，即无需针对新语言额外标注即可获得翻译能力。此次部署标志着该技术从实验室研究走向大众可用的系统级产品。

**「影响」** 对 Pixel 11 上的聋人和听障用户而言，这是手语 AI 首次直接进入日常消费产品，可借助 Gboard 进行手语输入，并通过 Live Transcribe 获得实时字幕。由于目前仅支持美国手语转英语，其他语言和手语用户仍需等待后续扩展。

**标签**: `#sign language AI`, `#DeepMind`, `#accessibility`, `#machine translation`, `#consumer AI`

---

## 时政综合

<a id="item-world-news-1"></a>
### [刚果（金）埃博拉疫情扩散至第六个省份](https://www.theguardian.com/world/2026/aug/13/ebola-drc-democratic-republic-congo-sixth-province) ⭐️ 9.0/10

刚果（金）埃博拉疫情已蔓延至第六个省。最新政府数据显示，疫情已造成超过 4500 例病例、2100 多人死亡；世卫组织负责人表示，此次疫情可能成为有记录以来最致命的一次，超过 2014-2016 年西非疫情（至少 1.1 万人死亡）。

rss · Guardian World · 8月13日 15:17

**「背景」** 埃博拉是一种高致死率病毒性出血热；这是刚果（金）第 17 次埃博拉疫情，始于 2026 年 5 月伊图里省，距上一次疫情结束仅五个月。

**「影响」** 世卫组织表示，此次疫情可能超过 2014-2016 年西非疫情至少 1.1 万人的死亡规模，成为有记录以来最致命的埃博拉疫情；疫情已扩散至第六个省，周边地区的防控压力随之加大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_Ebola_epidemic">2026 Ebola epidemic - Wikipedia</a></li>
<li><a href="https://www.theguardian.com/world/2026/aug/13/ebola-drc-democratic-republic-congo-sixth-province">DRC’s fast-growing Ebola outbreak spreads to sixth province | Ebola | The Guardian</a></li>
<li><a href="https://www.orlandosentinel.com/2026/08/13/ebola-outbreak-spread-new-province-congo/">Ebola outbreak has spread to new province in Congo: head of Africa CDC</a></li>

</ul>
</details>

**标签**: `#Ebola`, `#DRC`, `#Public Health`, `#WHO`, `#Outbreak`

---

