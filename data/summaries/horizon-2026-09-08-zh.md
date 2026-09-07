# Horizon 每日速递 - 2026-09-08

> 从 109 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [LG 智能电视在关屏状态下记录音频并窥探本地网络](#item-tech-news-1) ⭐️ 8.0/10
2. [OpenAI 揭示编码代理重塑研究工作](#item-tech-news-2) ⭐️ 8.0/10
3. [TPU 推理外部化加速：InferenceX 性能提升 50%](#item-tech-news-3) ⭐️ 8.0/10
4. [LLM 引导的程序进化改进 10 个最佳圆填充解](#item-tech-news-4) ⭐️ 8.0/10
5. [将 KV 缓存作为智能体运行时](#item-tech-news-5) ⭐️ 8.0/10
6. [基于 31352 次重复测量的 LLM 性能漂移观察与方法](#item-tech-news-6) ⭐️ 8.0/10
7. [华为发布 Mate XT 2 及麒麟 9050 Pro 芯片](#item-tech-news-7) ⭐️ 8.0/10
8. [最高法发布 AI 纠纷司法解释，明确换脸与算法杀熟责任](#item-tech-news-8) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [LG 智能电视在关屏状态下记录音频并窥探本地网络](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

一项安全分析显示，LG 智能电视在屏幕关闭的情况下仍在记录音频，并主动扫描本地网络设备，引发了严重的隐私担忧。该问题影响了庞大的用户群体，揭示了 LG 智能电视在隐私保护方面的重大漏洞，包括未经授权的音频收集和网络流量监控。尽管 LG 的服务条款要求用户告知可能被录音的第三方，但这一行为仍引发了关于法律合规性和用户知情权的广泛讨论。

hackernews · treve · 9月7日 00:22 · [社区讨论](https://news.ycombinator.com/item?id=49592375)

**「背景」** LG 智能电视是集成了网络连接和语音控制功能的消费电子产品，通常运行专有操作系统以支持流媒体服务和智能交互。这些设备通常配备麦克风以实现语音指令功能，并连接 Wi-Fi 以访问在线内容，这使其成为物联网生态系统的一部分。由于此类设备长期处于通电状态并接入家庭局域网，其数据收集行为和隐私政策一直是安全研究人员关注的焦点。

**「社区讨论」** 社区成员对 LG 的服务条款表示强烈不满，指出条款要求用户必须告知所有可能被录音的访客，这在实际操作中几乎不可能实现。部分用户分享了断开电视网络连接或物理拆除无线模块的应对措施，并讨论了此类行为可能违反窃听法的法律风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html">LG smart TVs caught logging audio with screen off and snooping ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#hardware`, `#iot`, `#lg`

---

<a id="item-tech-news-2"></a>
### [OpenAI 揭示编码代理重塑研究工作](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 8.0/10

OpenAI 发布了关于其内部研究团队使用编码代理的详细报告，并暗示“递归自我改进”（RSI）可能成为其新的通用人工智能（AGI）方向。报告显示，2026 年代理工程在 OpenAI 内部迅速普及，一张图表显示每位研究员的日均 AI 计算支出从 2 月份接近零的水平，在 4 月至 6 月间缓慢增长至约 150 美元，随后在 7 月底至 8 月期间急剧攀升至约 600 美元。作者推测，这一显著加速可能与内部员工在 7 月下旬获得了后来作为 GPT-6 Astra 发布的模型访问权限有关。

rss · Simon Willison · 9月6日 23:57

**「背景」** 递归自我改进（Recursive Self-Improvement，简称 RSI）是指人工智能系统通过自主修改自身代码或架构来提升性能的能力，常被视为通往通用人工智能（AGI）的关键路径之一。OpenAI 的研究流程涉及设计改进方案、编写评估代码、构建测试基础设施以及集成核心训练等多个步骤，其中编写代码和运行实验是研究人员的核心活动。随着智能体工程在 2026 年的兴起，OpenAI 内部开始广泛采用编码代理来加速这些研究环节，从而推动整体研究能力的提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.petertheil.com/160418/">(Recursive Self-Improvement) Research acceleration: The view inside OpenAI - Peter Theil</a></li>
<li><a href="https://openai.com/index/research-acceleration-view-inside-openai/">Research acceleration: The view inside OpenAI | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AGI`, `#Coding Agents`, `#Recursive Self-Improvement`, `#AI Research`

---

<a id="item-tech-news-3"></a>
### [TPU 推理外部化加速：InferenceX 性能提升 50%](https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam) ⭐️ 8.0/10

InferenceX 通过快速外部化 TPU 技术栈，实现了高达 50%的性价比提升，旨在挑战 CUDA 的主导地位。该技术引入了 TPUv8i 等新硬件和 Ironwood 等新工具，显著优化了云 AI 能力。随着客户基础的不断增长，这一进展标志着 AI 基础设施领域的重大转变，为开发者提供了除 NVIDIA 之外的高性能推理选择。

rss · Semianalysis · 9月7日 20:00

**「背景」** TPU（张量处理单元）是谷歌为加速机器学习工作负载而设计的专用集成电路，长期以来主要用于谷歌内部服务。CUDA 是英伟达开发的并行计算平台和编程模型，构成了 AI 硬件生态中难以逾越的护城河。InferenceX 是谷歌推出的新软件栈，旨在将 TPU 技术对外开放，以支持外部客户进行 AI 推理任务。

**「影响」** TPU v8i 在低延迟目标下相比 Ironwood TPU 提供了高达 80% 的性价比提升，这为运行大型混合专家模型的用户带来了显著的成本优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/tpu-inferencex-full-steam">TPU Inference Externalization Full Steam Ahead - InferenceX</a></li>
<li><a href="https://io-fund.com/ai-stocks/google-tpu-v8-vs-nvidia-inference-rewrites-ai-market">Google TPU v8 vs Nvidia: How Inference Is Rewriting the AI Market</a></li>

</ul>
</details>

**标签**: `#TPU`, `#Inference`, `#Hardware`, `#AI Infrastructure`, `#Cloud Computing`

---

<a id="item-tech-news-4"></a>
### [LLM 引导的程序进化改进 10 个最佳圆填充解](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

一种 LLM 引导的程序进化方法通过迭代提出和验证算法变更，改进了 Packomania 基准测试中 10 个已知的最佳圆填充解决方案。该方法从一个简单的种子求解器开始，利用 LLM 根据结果记分板和尝试历史提出算法变更，并通过独立验证器对候选方案进行评分以保留改进。在 Packomania csqv 基准测试中，该方法在 15 次迭代内将 N 值从 101 到 114 的 10 个最佳半径总和提高了 2.4%至 5.4%，总 LLM 成本为 27.72 美元。Packomania 已独立接受了这些结果，相关论文和代码已公开发布。

reddit · r/MachineLearning · /u/SIGH\_I\_CALL · 9月7日 16:54

**「背景」** 圆填充问题是指在单位正方形内放置 N 个半径可变的圆，以最大化这些圆的半径总和，这是一个经典的计算几何与组合优化难题。Packomania 网站维护着该问题的基准测试数据，记录了不同 N 值下已知的最优解及其坐标。LLM 引导的程序进化是一种优化方法，通过语言模型迭代修改完整的程序代码，并利用可执行程序的评估结果来筛选和保留性能更优的版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.packomania.com/csqv/csqv.html">The best known packings of variable-sized circles in a square with maximized sum of radii (complete up to N</a></li>
<li><a href="https://arxiv.org/html/2609.05093">LLM - Guided Program Evolution for Circle Packing:Breaking 10...</a></li>
<li><a href="https://www.openai-hub.com/news/1937/">LLM 引导程序进化刷新圆打包纪录：15轮提升5.4% - OpenAI Hub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#optimization`, `#program synthesis`, `#benchmark results`, `#circle packing`

---

<a id="item-tech-news-5"></a>
### [将 KV 缓存作为智能体运行时](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

研究团队提出了一种通过修改模型推理状态（即 KV 缓存）来实现大语言模型（LLM）更高交互性和响应性的替代方法。该概念建立在团队此前发表的 Hogwild\! Inference 和 AsyncReasoning 论文基础之上，并展示了未来的工作预览，即使用类似技术让 Qwen3.8-27B 智能体在 DOOM 环境中进行交互式游戏。研究人员探讨了模型推理或运行时设计是否应作为介于模型本身与抽象控制框架之间、且未被充分探索的智能体能力维度。

reddit · r/MachineLearning · /u/\_puhsu · 9月7日 09:03

**「背景」** KV 缓存通常作为自回归推理中的解码优化手段，用于存储先前 Token 计算出的键值对，从而避免在每一步重新计算完整前缀。Yandex 研究团队此前提出的 Hogwild\! Inference 和 AsyncReasoning 等方法，通过共享 KV 缓存或划分推理流（如用户信息、私有推理和公共输出）来探索并行生成。这些研究将 KV 缓存视为一种可编程的轻量级运行时，而不仅仅是加速技巧，旨在通过多路复用缓存段来处理并发子任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.yandex.com/blog/the-kv-cache-as-an-agent-runtime">The KV cache as an agent runtime | Yandex Research</a></li>
<li><a href="https://aitechinspire.com/stop-tuning-start-orchestrating-the-kv-cache-as-an-agent-runtime/">Stop Tuning, Start Orchestrating: The KV Cache as an Agent Runtime</a></li>
<li><a href="https://ai.plainenglish.io/hogwild-inference-parallel-llm-generation-via-concurrent-attention-8cbce271cba2">Hogwild ! Inference : Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://research.yandex.com/blog/the-kv-cache-as-an-agent-runtime">The KV cache as an agent runtime | Yandex Research</a></li>

</ul>
</details>

**标签**: `#LLM Agents`, `#KV Cache`, `#Model Inference`, `#Research`, `#System Architecture`

---

<a id="item-tech-news-6"></a>
### [基于 31352 次重复测量的 LLM 性能漂移观察与方法](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 8.0/10

一项针对 49 个模型进行的纵向分析涵盖了 31,352 次重复基准测试测量，旨在检测 API 服务模型随时间发生的行为变化。数据显示，日内分数的标准差为 2.80 分，而日间中位数标准差为 8.43 分，两者比例约为 3:1，表明时间变异性显著。作者强调不应将基准测试视为静态的排行榜问题，而应关注模型相对于自身基线的行为差异，并区分能力变化与基础设施可用性问题。为了解决基准测试污染问题，该方法论在保持科学可审查性的同时，选择不公开具体的实时任务库和部分操作参数。

reddit · r/MachineLearning · /u/ionutvi · 9月7日 07:44

**「背景」** 传统的 LLM 基准测试通常被视为评估模型能力的静态快照，但 API 服务模型背后的基础设施、配置和版本可能会随时间变化，导致模型行为发生不可见的漂移。这种动态性使得仅依赖单一时间点的评分无法准确反映模型在生产环境中的长期稳定性和可靠性。

**标签**: `#LLM`, `#Benchmarks`, `#Model Evaluation`, `#Performance Drift`, `#MLOps`

---

<a id="item-tech-news-7"></a>
### [华为发布 Mate XT 2 及麒麟 9050 Pro 芯片](https://www.news.cn/20260907/adf46c5c003240d28cc3cf6de54f9b5f/c.html) ⭐️ 8.0/10

华为于 7 日在广州发布了 Mate XT 2 三折叠手机，该手机搭载了最新的麒麟 9050 Pro 芯片。这是首款采用逻辑折叠技术的高性能芯片，通过在单芯片内分层排布逻辑单元并增设垂直互联通道，实现了更短的信号传输路径、更低的时延以及更好的性能。此次发布标志着华为继 Mate40 全球发布会之后，时隔六年在旗舰发布会上再次推出全新的麒麟芯片。

telegram · zaihuapd · 9月7日 08:20

**「背景」** 华为的麒麟芯片曾是其旗舰手机的核心组件，但近年来因外部制裁导致高性能芯片供应受限，上一代旗舰芯片麒麟 9000 系列发布于 2020 年。此次发布的 Mate XT 2 是华为推出的三折叠屏手机，采用了新的 LogicFolding 架构，旨在通过 3D 堆叠技术提升芯片性能。这一架构基于华为提出的 Tau Scaling Law，标志着其在半导体设计上的新尝试。

**「影响」** 华为通过 Mate XT 2 重新进入高性能旗舰芯片市场，为消费者提供了采用逻辑折叠技术以降低时延的移动设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huaweicentral.com/huawei-mate-xt-2-launched/">Huawei Mate XT 2 launched with 10.2-inch inward folding display and Kirin 9050 Pro chipset - Huawei Central</a></li>
<li><a href="https://www.digitimes.com/news/a20260907VL215/huawei-kirin-flagship-smartphone-launch-performance.html">Huawei Kirin 9050 Pro revives flagship chip launches with reported LogicFolding architecture in Mate XT 2</a></li>

</ul>
</details>

**标签**: `#Hardware`, `#Semiconductors`, `#Mobile Devices`, `#Huawei`, `#3D Integration`

---

<a id="item-tech-news-8"></a>
### [最高法发布 AI 纠纷司法解释，明确换脸与算法杀熟责任](https://www.cnr.cn/news/20260907/t20260907_527806795.shtml) ⭐️ 8.0/10

最高人民法院于 9 月 7 日发布关于人工智能纠纷案件的司法解释，共 5 部分 24 条，重点规范 AI 换脸、算法杀熟、冒充他人代言、自动驾驶及知识产权等领域的法律问题。该解释明确，未经同意使用 AI 制作可识别的人脸或声音可能构成人格权侵权，实施算法价格歧视侵害权益的应承担责任，且对于 AI 冒充他人代言诱导消费的行为，法院可依法支持惩罚性赔偿请求。此外，解释还依法规制利用人工智能实施“网络开盒”或“人肉搜索”等侵害自然人隐私权的行为。

telegram · zaihuapd · 9月7日 09:32

**「背景」** 随着人工智能技术的广泛应用，AI 换脸、算法价格歧视（即“杀熟”）以及冒充他人代言等新型侵权行为日益增多，引发了关于人格权、隐私保护和消费者权益的法律争议。此前，针对这些具体技术场景的法律责任界定在司法实践中存在模糊地带，导致案件审理标准不一。此次最高人民法院发布的司法解释旨在填补这一空白，为处理涉及人工智能的纠纷案件提供明确的法律依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://t.me/zaihuapd/43664">科技圈 在花频道– Telegram</a></li>

</ul>
</details>

**标签**: `#AI Regulation`, `#Legal`, `#Deepfake`, `#Algorithmic Bias`, `#Privacy`

---

