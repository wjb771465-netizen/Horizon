# Horizon 每日速递 - 2026-09-11

> 从 124 条内容中筛选出 11 条重要资讯。

---

**科技新闻**
1. [AI 辅助开发的 WeChat 零点击蠕虫 WeWorm](#item-tech-news-1) ⭐️ 9.0/10
2. [OpenAI 推出 GPT-Live-1 API 支持全双工语音通话](#item-tech-news-2) ⭐️ 9.0/10
3. [DeepSeek 发布 V4.1 Flash 模型](#item-tech-news-3) ⭐️ 9.0/10
4. [Shopify 从 React Native 迁移回 Swift 和 Kotlin](#item-tech-news-4) ⭐️ 8.0/10
5. [微软将 Rust 列为一级语言](#item-tech-news-5) ⭐️ 8.0/10
6. [利用 Codex 和 ChatGPT 搜索新型抗菌分子](#item-tech-news-6) ⭐️ 8.0/10
7. [OpenAI 在 ChatGPT Work 中推出数据代理](#item-tech-news-7) ⭐️ 8.0/10
8. [OpenAI 推出面向金融服务的 ChatGPT](#item-tech-news-8) ⭐️ 8.0/10
9. [OpenAI 推出 Agents API](#item-tech-news-9) ⭐️ 8.0/10
10. [蚂蚁国际与 Visa、Mastercard 合作开发 AI 支付标准](#item-tech-news-10) ⭐️ 8.0/10
11. [DeepSelect：面向 DSA 与采样器的 TopK 内核](#item-tech-news-11) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [AI 辅助开发的 WeChat 零点击蠕虫 WeWorm](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 演示，这是首个通过 WeChat 通话在 iOS 和 Android 设备上传播的零点击蠕虫。受害者无需接听电话或与手机进行任何交互即可被利用，即使接听也听不到任何声音。研究团队在 AI 辅助下仅用约两天时间就发现了漏洞并编写了首个远程代码执行（RCE）漏洞利用程序，随后仅用一周时间构建了蠕虫。这种规模的蠕虫开发过去通常需要大型团队花费数月时间，而 AI 在此过程中完成了大部分工作。

rss · Simon Willison · 9月10日 00:56

**「背景」** 零点击漏洞是一种无需目标用户进行任何交互（如点击链接或接听电话）即可被利用的安全缺陷，常被用于高度复杂的移动攻击。WeChat（微信）拥有庞大的全球用户群，其跨平台特性使其成为安全研究的重要目标，而 VoIP（网络语音电话）功能因其处理实时数据流的复杂性，常成为内存破坏漏洞的潜在来源。传统的漏洞挖掘和利用开发通常需要安全专家耗费数月时间进行逆向工程和模糊测试，而生成式 AI 的引入正在改变这一流程，通过自动化代码分析和漏洞模式识别来加速发现过程。

**「影响」** 这一进展表明 AI 大幅降低了开发复杂移动漏洞利用的门槛，将原本耗时数月的工作缩短至一周多，从而可能加速高危漏洞的发现与武器化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://calif.io/research/weworm">The first zero - click worm to spread through WeChat calls across iOS...</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lwa1BUNUVSRVpLbmNGUWRpaDFDZ0FQAQ?hl=en-PH&amp;gl=PH&amp;ceid=PH:en">Google News - Calif uses AI to discover zero - click WeChat ...</a></li>
<li><a href="https://www.youtube.com/watch?v=neVzPnUyrtw">Researchers Built an AI Worm That Hijacks WeChat by... - YouTube</a></li>

</ul>
</details>

**标签**: `#security`, `#ai`, `#malware`, `#mobile`, `#vulnerability-research`

---

<a id="item-tech-news-2"></a>
### [OpenAI 推出 GPT-Live-1 API 支持全双工语音通话](https://openai.com/index/introducing-gpt-live-1-in-the-api) ⭐️ 9.0/10

OpenAI 发布了名为 GPT-Live-1 的新 API 模型，将自然、全双工的语音对话引入开发者生态系统。该模型具备更强的指令遵循能力，支持自定义语音以及电话集成功能，旨在帮助开发者构建低延迟的实时语音体验。这一更新标志着语音交互技术的范式转变，通过允许同时进行语音输入和输出，显著提升了对话的自然度。

rss · OpenAI Blog · 9月10日 00:00

**「背景」** 传统的语音交互通常依赖自动语音识别（ASR）将音频转换为文本，再由大语言模型处理，最后通过文本转语音（TTS）生成音频，这种多步骤流程往往导致数秒的延迟。GPT-4o 等新一代模型通过直接在潜在空间处理音频，完全绕过文本转录环节，将内部模型延迟降低至 80 毫秒到 120 毫秒。这种架构支持全双工通信和流式处理，使得系统能够像人类对话一样自然地处理打断和实时交互。

**「影响」** 开发人员现在可以构建实时、低延迟的语音应用程序，这些应用程序能够处理连续的、全双工的对话，而无需等待轮流发言，从而显著改善客户服务等复杂交互场景中的用户体验。尽管电话线路的音频限制可能会影响特定数据（如数字和名称）的识别准确性，但该模型的原生音频处理能力为实时语音交互设立了新的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.autointerviewai.com/blog/openai-gpt4o-realtime-voice-api-deep-dive-2026">OpenAI GPT-4o Realtime Voice API Review: Architecture, Latency Benchmarks, and True Production Costs in 2026 | Auto Interview AI</a></li>
<li><a href="https://github.com/openclaw/openclaw/issues/5606">feat(voice-call): OpenAI Realtime API voice-to-voice mode for sub-second latency · Issue #5606 · openclaw/openclaw</a></li>
<li><a href="https://explore.n1n.ai/blog/how-openai-scales-low-latency-realtime-voice-ai-2026-05-05">How OpenAI Scales Low Latency Realtime Voice AI | Enterprise Unified LLM API Gateway (One Key for All Models) | n1n.ai</a></li>
<li><a href="https://arxiv.org/html/2603.13686v1">𝜏-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-gpt-live-1-openai-voice-model">What Is GPT Live 1? OpenAI&#x27;s Full-Duplex Voice Model Explained | MindStudio</a></li>
<li><a href="https://www.voxfra.com/blog/what-is-full-duplex-voice-ai">What Is Full-Duplex Voice AI? Cascaded vs. Turn-Based vs. Full-Duplex Explained — Voxfra</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Voice AI`, `#API`, `#Real-time Communication`, `#Telephony`

---

<a id="item-tech-news-3"></a>
### [DeepSeek 发布 V4.1 Flash 模型](https://mp.weixin.qq.com/s/qg0NU3NNUbp1co2PdkAPAg) ⭐️ 9.0/10

DeepSeek 正式发布了 V4.1 Flash 模型，这是其全新模型结构系列中尺寸最小的成员。该模型采用 552B 参数的 Causal-Encoder-Decoder 结构，输入和输出激活分别为 8B 和 16B，并原生支持多模态视觉理解。DeepSeek API 已上线该模型，新价格将于 2026 年 9 月 10 日 12:00 生效。此外，自 9 月 14 日 12:00 起，deepseek-v4-pro 的请求将自动路由至 V4.1 Flash 并按新价格计费。

telegram · zaihuapd · 9月10日 05:54

**「背景」** DeepSeek V4.1 Flash 采用了 Causal Encoder-Decoder（CED）架构，这是一种由因果编码器和解码器组成的混合专家模型，总参数量达 552B，但在处理输入和输出时分别仅激活 8B 和 16B 参数。这种架构设计旨在通过减少推理时的活跃参数量来提高效率，同时原生支持多模态视觉理解能力。该模型是 DeepSeek 全新模型结构系列中的最小尺寸版本，其性能据称已超越此前的旗舰模型 DeepSeek-V4-Pro。

**「影响」** 从 2026 年 9 月 14 日 12:00 起，发送至 deepseek-v4-pro 的请求将自动路由至 V4.1 Flash 并按新价格计费，直至未来 V4.1 Pro 发布【tool-2-1】。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek-ai/DeepSeek-V4.1-Flash · Hugging Face</a></li>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.</a></li>
<li><a href="https://alphasignal.ai/news/deepseek-s-v4-1-flash-beats-its-own-flagship-at-a-quarter-of-the-memory-cost">DeepSeek&#x27;s V4.1-Flash Beats Its Own Flagship at a Quarter of the Memory Cost | AlphaSignal</a></li>
<li><a href="https://api-docs.deepseek.com/quick_start/pricing/">Models &amp; Pricing | DeepSeek API Docs</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#Large Language Models`, `#Multimodal AI`, `#Model Release`, `#API Update`

---

<a id="item-tech-news-4"></a>
### [Shopify 从 React Native 迁移回 Swift 和 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 详细阐述了其将移动应用从 React Native 迁移回原生 Swift 和 Kotlin 的战略决策，并利用 AI 工具克服了代码重写的成本障碍。这一举措挑战了当前跨平台框架的主导地位，引发了关于跨平台与原生开发之间权衡的广泛行业讨论。Shopify 的技术深入分析展示了如何通过自动化工具降低迁移成本，为工程团队提供了宝贵的实践经验。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**「背景」** Shopify 在 2020 年曾宣布 React Native 是其移动开发的未来，旨在通过跨平台框架避免重复构建功能并允许跨栈工作【tool-1-2】。然而，随着 AI 代理在代码实现、翻译、测试和审查方面能力的提升，维护双原生代码库的成本显著降低，促使该公司在 2026 年 9 月决定将所有移动应用迁移回 Swift 和 Kotlin【tool-1-2】【tool-1-3】。这一转变标志着技术策略的重大调整，从依赖单一跨平台技术栈回归到针对特定平台优化的原生开发模式。

**「社区讨论」** 社区成员对这一迁移决策反应不一，部分人分享了类似的成功经验，指出 AI 工具显著加速了迁移过程，而另一些人则质疑 LLM 在降低迁移成本中的实际作用。有评论强调，虽然跨平台框架初期能减少人力成本，但长期来看，原生平台仍需专门的技术专家进行优化，且随着代码生成技术的进步，React Native 的优势正在减弱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/jamilxt/shopify-is-moving-its-mobile-apps-back-to-native-coding-agents-made-it-cheaper-to-build-twice-than-4bf9">Shopify Is Moving Its Mobile Apps Back to Native. Coding ...</a></li>
<li><a href="https://picx.dev/news/LsT33N">Shopify moves from React Native back to native Swift and ...</a></li>

</ul>
</details>

**标签**: `#mobile development`, `#react native`, `#swift`, `#kotlin`, `#software architecture`

---

<a id="item-tech-news-5"></a>
### [微软将 Rust 列为一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

微软正式将 Rust 指定为其内部的一级语言，标志着该公司在系统编程和内存安全改进方面做出了重大承诺。这一举措意味着微软将在其工程生态系统中给予 Rust 与 C++ 和 C\# 等传统语言同等的地位，并可能涉及大规模的代码迁移计划。社区讨论指出，此举旨在解决微软产品组合中大量存在的内存安全漏洞，据称其中 70% 的 CVE 属于此类问题。此外，有评论提到微软已将 LLVM 替换为 MSVC 后端，并证实了关于 MSVC 集成的传闻。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**「背景」** Rust 是一种专注于内存安全、并发和性能的系统编程语言，旨在解决 C 和 C++ 等语言中常见的内存错误问题。微软拥有庞大的 C++ 代码库，长期以来一直致力于通过引入更安全的语言来减少安全漏洞。此次宣布 Rust 成为微软的一级语言，意味着该语言在公司内部获得了与 C++ 等传统语言同等的支持地位和资源投入。

**「社区讨论」** 社区成员认为这一声明证明了 Rust 已不再是实验性语言，而是 C++ 和 C\# 等成熟语言的严肃竞争对手，特别是在与 Zig 和 Odin 等较新的“更好的 C/C++”语言相比时。讨论还强调了微软计划通过自动化工具在 2030 年前将 10 亿行代码转换为 Rust 的雄心，以及所有主要操作系统供应商现在都在系统编程语言选择上实现多元化的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Software Engineering`

---

<a id="item-tech-news-6"></a>
### [利用 Codex 和 ChatGPT 搜索新型抗菌分子](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 8.0/10

César de la Fuente 实验室利用 Codex 和 ChatGPT 扫描现存及已灭绝生物的基因组，以寻找能够对抗耐药性感染的新型抗菌分子候选物。这项研究将生成式人工智能应用于计算生物学领域，旨在解决全球面临的抗菌素耐药性这一重大公共卫生威胁。通过分析海量基因组数据，该团队探索了大型语言模型在传统软件工程之外的科学发现潜力。

rss · OpenAI Blog · 9月10日 16:00

**「背景」** 抗菌素耐药性已成为全球公共卫生的重大威胁，迫切需要发现新型抗菌分子以应对传统抗生素失效的挑战。计算生物学利用算法分析生物数据，正在加速药物发现过程，而生成式人工智能模型如 Codex 和 ChatGPT 通常用于代码生成和文本处理。César de la Fuente 实验室的创新之处在于，将这些原本用于软件工程的模型应用于扫描现存的和已灭绝生物的基因组，以寻找具有潜在抗菌特性的分子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials/">How a researcher uses Codex and ChatGPT to search for new ...</a></li>
<li><a href="https://www.jurelist.com/news/cesar-de-la-fuente-s-lab-uses-codex-and-chatgpt-to-search-genomes-for-antimicrob-a30c0fdf">César de la Fuente’s Lab Uses Codex and ChatGPT to Search ...</a></li>

</ul>
</details>

**标签**: `#AI in Science`, `#Bioinformatics`, `#Antimicrobial Resistance`, `#Generative AI`, `#Computational Biology`

---

<a id="item-tech-news-7"></a>
### [OpenAI 在 ChatGPT Work 中推出数据代理](https://openai.com/index/put-data-to-work) ⭐️ 8.0/10

OpenAI 在 ChatGPT Work 中推出了数据代理功能，允许用户连接公司数据并使用自然语言生成洞察和交互式仪表板。该功能旨在通过 AI 弥合自然语言与数据分析之间的差距，帮助企业用户更高效地处理业务数据。用户无需编写代码，即可通过对话方式挖掘数据价值并构建可视化报表。这一更新主要面向企业用户，旨在提升生产力并优化业务工作流程中的 AI 集成体验。

rss · OpenAI Blog · 9月10日 15:00

**「背景」** ChatGPT 是由 OpenAI 开发的生成式人工智能聊天机器人，利用大型语言模型根据用户提示生成文本、语音和图像。ChatGPT Work 是面向企业用户的版本，旨在集成 AI 到业务工作流程中以提高生产力。Data agent 是该平台内的一项新功能，允许用户通过自然语言连接公司数据源，从而将数据转化为答案、交互式仪表盘和可执行的操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChatGPT">ChatGPT - Wikipedia</a></li>
<li><a href="https://openai.com/index/put-data-to-work/">Now everyone can put data to work | OpenAI</a></li>
<li><a href="https://www.youtube.com/watch?v=MSiAd36bGeQ">Data agent in ChatGPT Work - YouTube</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#Data Analysis`, `#Enterprise AI`, `#Productivity`

---

<a id="item-tech-news-8"></a>
### [OpenAI 推出面向金融服务的 ChatGPT](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 8.0/10

OpenAI 正式推出了面向金融服务的 ChatGPT 版本，该版本结合了内置的金融数据与 GPT-6 Astra 模型。这一新工具旨在支持金融研究、建模工作以及生成面向客户的材料，以满足金融行业的专业需求。通过集成特定的金融数据集，该服务能够提供更精准的行业洞察和分析能力。这一举措标志着 OpenAI 在企业级 AI 部署领域针对特定垂直行业的进一步深化。

rss · OpenAI Blog · 9月10日 07:00

**「背景」** ChatGPT for Financial Services 是 OpenAI 推出的定制化 ChatGPT Work 体验，旨在为金融机构提供专门的 AI 辅助工具。该服务将内置的金融数据与 GPT-6 Astra 模型的推理能力相结合，以支持团队开展研究、构建财务模型以及制作客户定制材料。这一产品属于 OpenAI 企业级生产力套件的一部分，强调在提升效率的同时保持企业治理和审计追踪能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-financial-services/">Introducing ChatGPT for Financial Services | OpenAI</a></li>
<li><a href="https://www.macobserver.com/news/openai-launches-chatgpt-for-financial-services-gpt-6-astra/">OpenAI Launches ChatGPT for Financial Services With GPT-6 Astra</a></li>
<li><a href="https://venturebeat.com/data/openai-launches-chatgpt-for-financial-services-with-integrated-data-sources-it-pulls-research-cites-it-and-builds-decks-in-minutes">OpenAI launches ChatGPT for Financial Services with integrated data sources — it pulls research, cites it, and builds decks in minutes | VentureBeat</a></li>

</ul>
</details>

**标签**: `#AI`, `#Financial Services`, `#Enterprise Software`, `#GPT-6`, `#OpenAI`

---

<a id="item-tech-news-9"></a>
### [OpenAI 推出 Agents API](https://openai.com/index/introducing-the-agents-api) ⭐️ 8.0/10

OpenAI 正式推出了 Agents API，这是一项旨在构建和启动云端代理的托管服务。该服务由 Codex harness 提供支持，专注于编排、长运行会话以及工具使用功能。这一 API 的发布为开发者提供了构建复杂 AI 系统的基础设施，能够处理需要多步骤推理和外部工具调用的任务。通过利用 Codex harness 进行编排，Agents API 旨在简化云端代理的开发和部署流程。

rss · OpenAI Blog · 9月10日 00:00

**「背景」** Codex harness 是一种用于编排 AI 智能体的架构框架，支持长运行会话、工具使用以及子智能体协调等关键模式。该框架采用 Apache-2.0 许可证开源，允许在商业产品中免费嵌入和修改，且在架构上不强制依赖 OpenAI 模型。OpenAI 现已推出基于此框架的 Agents API 托管服务，旨在简化云端智能体的构建与部署流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API | OpenAI</a></li>
<li><a href="https://www.newzv.com/ai-tools/openai-codex-harness-open-source/">OpenAI Open-Sources Codex Harness : The Numbers That... - NewzV</a></li>
<li><a href="https://gist.github.com/thehexbot/8fed6986e7315c1c6358fbd9109622d1">Agent Harness Architecture — Deep Analysis (March 2026) · GitHub</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Agents API`, `#Cloud Computing`, `#AI Orchestration`, `#Developer Tools`

---

<a id="item-tech-news-10"></a>
### [蚂蚁国际与 Visa、Mastercard 合作开发 AI 支付标准](https://www.cnbc.com/2026/09/10/ant-international-visa-mastercard-ai-agent-payment-standard.html) ⭐️ 8.0/10

蚂蚁国际宣布与 Visa 和 Mastercard 合作，共同为 AI 代理支付制定通用标准。三方将建立“了解你的代理”机制，通过将代理与有效实体关联、评估行为并监测风险，来提升不同支付系统间的互操作性和安全性。根据麦肯锡的预测，到 2030 年，AI 代理可能处理全球消费者商业交易中 3 万亿至 5 万亿美元的金额。

telegram · zaihuapd · 9月10日 03:00

**「背景」** AI 代理是指能够自主执行任务和进行决策的软件程序，随着其在商业领域的应用日益广泛，如何安全、高效地处理其发起的支付交易成为关键挑战。目前缺乏统一的技术标准，导致不同支付网络和系统之间难以实现无缝对接与风险管控。

**标签**: `#fintech`, `#AI agents`, `#payments`, `#standards`, `#security`

---

<a id="item-tech-news-11"></a>
### [DeepSelect：面向 DSA 与采样器的 TopK 内核](https://github.com/deepseek-ai/DeepSelect) ⭐️ 8.0/10

DeepSeek-AI 于 2026 年 9 月 10 日发布了 DeepSelect v1.0.0，这是一套专为 DeepSeek 稀疏注意力（DSA）和采样器设计的高性能 TopK 内核。该工具旨在优化大语言模型推理过程中的关键操作，相比原生 PyTorch 的 torch.topk 函数，能够实现 2 至 20 倍的性能加速。这一显著的性能提升有助于提高推理效率，降低计算资源消耗。

telegram · zaihuapd · 9月10日 07:28

**「背景」** DeepSeek 稀疏注意力（DSA）是一种基于内容的动态稀疏注意力机制，旨在实现极长上下文的高效扩展，同时保持与密集模型几乎相同的质量。该架构通过算法与硬件感知设计的结合，包括 FP8 执行和自定义 CUDA 内核，支持在大规模长序列代理 LLM 中的部署。TopK 内核是 DSA 和采样器中的关键组件，负责从大量数据中快速筛选出最重要的元素，DeepSelect 正是针对这一操作的高性能实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/deepseek-sparse-attention-dsa">DeepSeek Sparse Attention Mechanism (DSA)</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3.2-Exp">GitHub - deepseek-ai/DeepSeek-V3.2-Exp · GitHub</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSelect">GitHub - deepseek - ai / DeepSelect : DeepSelect : TopK kernels for...</a></li>

</ul>
</details>

**标签**: `#performance optimization`, `#deepseek`, `#inference`, `#kernels`, `#sparse attention`

---

