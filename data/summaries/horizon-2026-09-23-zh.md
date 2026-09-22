# Horizon 每日速递 - 2026-09-23

> 从 139 条内容中筛选出 8 条重要资讯。

---

**科技新闻**
1. [vLLM v0.30.0 发布：引入持久化 GPU 缓存与多款新模型](#item-tech-news-1) ⭐️ 9.0/10
2. [Claude Opus 5.5](#item-tech-news-2) ⭐️ 9.0/10
3. [GPT-6 提示词缓存重大改进](#item-tech-news-3) ⭐️ 9.0/10
4. [阿里发布宣称最强国产 AI 芯片真武 V900，算力提升至 3 倍](#item-tech-news-4) ⭐️ 9.0/10
5. [🤖 OpenAI 发布 GPT-6 Sol 与 Luna，API 降价五成](#item-tech-news-5) ⭐️ 9.0/10
6. [Xiaomi releases MiMo-V2.6: &quot;Frontier intelligence, all the modalities, built in public.&quot; \[N\]](#item-tech-news-6) ⭐️ 8.0/10
7. [Complex KDA 增强 Kimi Delta Attention 表达能力](#item-tech-news-7) ⭐️ 8.0/10

**时政综合**
1. [Trump’s threat to annihilate Iran to UN general assembly is stunning, even for him](#item-world-news-1) ⭐️ 9.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [vLLM v0.30.0 发布：引入持久化 GPU 缓存与多款新模型](https://github.com/vllm-project/vllm/releases/tag/v0.30.0) ⭐️ 9.0/10

vLLM v0.30.0 正式发布，包含来自 315 位贡献者的 762 项提交。该版本引入了持久化单 GPU 权重缓存守护进程，通过 CUDA IPC 映射权重实现快速重启，并新增了对 DeepSeek-V4.1-Flash、GLM-5.3-Flash 和 K2-Horizon 等前沿模型的支持。性能方面，Model Runner V2 实现了双批次重叠与全 CUDA 图捕获，将 H200 上的图捕获时间从 12 秒降至 2 秒；Kimi K3 和 Qwen3.8-Flash-Next 也获得了显著的内核加速与端到端吞吐量提升。此外，版本还加入了 Gumbel-max 水印生成与检测、HiSparse 主机驻留稀疏 MLA 解码层，以及针对特定目标的在线量化等功能，同时移除了 GPTQ 激活排序等破坏性变更。

github · khluu · 9月22日 05:20

**「背景」** vLLM 是一个广泛使用的高吞吐量开源大语言模型（LLM）推理与服务引擎。随着模型规模和上下文长度的不断增长，推理框架在快速启动、显存管理、长序列解码以及异构硬件适配方面面临着日益严峻的挑战，这促使 vLLM 不断在架构和内核层面进行深度优化。

**「影响」** 此次更新将显著降低生产环境中 vLLM 引擎重启的停机时间，并为运行 DeepSeek-V4 等稀疏大模型的开发者提供更高的解码吞吐量与更低的内核延迟。升级用户需注意破坏性变更，如 GPTQ 激活排序（g\_idx）的移除以及部分环境变量和启动参数的废弃。

**标签**: `#llm-inference`, `#vllm`, `#deepseek`, `#hardware-optimization`, `#open-source`

---

<a id="item-tech-news-2"></a>
### [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) ⭐️ 9.0/10

Anthropic releases Claude Opus 5.5, featuring notable price reductions, improved communication and writing quality, and enhanced performance, sparking substantial community discussion on frontier pacing and cost efficiency.

hackernews · km144 · 9月22日 16:29 · [社区讨论](https://news.ycombinator.com/item?id=49803892)

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#Pricing`, `#Frontier Models`

---

<a id="item-tech-news-3"></a>
### [GPT-6 提示词缓存重大改进](https://openai.com/index/better-prompt-caching-for-gpt-6) ⭐️ 9.0/10

OpenAI 宣布对 GPT-6 的提示词缓存功能进行重大改进，引入了更高的缓存命中率、全新的诊断工具以及显式断点控制。这些更新旨在显著降低 API 调用的延迟和成本，为开发者提供更精细的缓存管理能力。通过显式断点，开发者可以更精确地控制缓存边界，从而优化重复提示词的处理效率。

rss · OpenAI Blog · 9月22日 21:00

**「背景」** 提示词缓存（Prompt caching）是一种通过复用先前计算的结果来避免重复处理相同输入前缀的优化技术，能够显著降低大语言模型的推理延迟和 API 调用成本。此前，OpenAI 已为部分模型提供该功能，但受限于较短的缓存重用时间窗口和缺乏显式控制，难以满足持久化智能体等复杂应用场景的需求。此次 GPT-6 的更新将缓存重用窗口延长至 30 分钟，并引入了显式断点和诊断工具，使开发者能更稳定地利用缓存机制。

**「影响」** 使用 GPT-6 的 AI 开发者和企业将直接受益于更低的 API 延迟和计算成本，尤其是在处理具有大量重复前缀的提示词时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.brocker.org/openai-improved-prompt-caching-gpt-6-30-minute-window">OpenAI improves GPT - 6 prompt caching with 30-min window</a></li>

</ul>
</details>

**标签**: `#artificial intelligence`, `#large language models`, `#prompt caching`, `#OpenAI`, `#performance optimization`

---

<a id="item-tech-news-4"></a>
### [阿里发布宣称最强国产 AI 芯片真武 V900，算力提升至 3 倍](https://finance.sina.com.cn/stock/bxjj/2026-09-22/doc-inissitf7048094.shtml) ⭐️ 9.0/10

Alibaba&\#x27;s Pingtouge announced the Zhenwu V900 AI chip at the 2026 Yunqi Conference, claiming a 3x compute increase over its predecessor and 500k-card cluster scalability to support 2T parameter model inference.

telegram · zaihuapd · 9月22日 03:30

**标签**: `#AI Chips`, `#Hardware`, `#Alibaba`, `#Large Language Models`, `#Cloud Infrastructure`

---

<a id="item-tech-news-5"></a>
### [🤖 OpenAI 发布 GPT-6 Sol 与 Luna，API 降价五成](https://openai.com/index/introducing-gpt-6-sol-and-luna/) ⭐️ 9.0/10

OpenAI has released GPT-6 Sol and Luna models, offering capabilities close to GPT-6 Astra at a 50% reduction in API input and output prices compared to GPT-5.6.

telegram · zaihuapd · 9月22日 18:04

**标签**: `#Artificial Intelligence`, `#Large Language Models`, `#API Pricing`, `#OpenAI`, `#Software Engineering`

---

<a id="item-tech-news-6"></a>
### [Xiaomi releases MiMo-V2.6: &quot;Frontier intelligence, all the modalities, built in public.&quot; \[N\]](https://www.reddit.com/r/MachineLearning/comments/1wn36d4/xiaomi_releases_mimov26_frontier_intelligence_all/) ⭐️ 8.0/10

Xiaomi releases MiMo-V2.6, a frontier multimodal model with a reported $3.5M RL training cost and a live benchmarking dashboard.

reddit · r/MachineLearning · /u/we\_are\_mammals · 9月22日 07:56

**标签**: `#machine\_learning`, `#multimodal\_ai`, `#open\_models`, `#reinforcement\_learning`, `#benchmarking`

---

<a id="item-tech-news-7"></a>
### [Complex KDA 增强 Kimi Delta Attention 表达能力](https://www.reddit.com/r/MachineLearning/comments/1wn5uv9/understanding_and_enhancing_kimi_delta_attention_r/) ⭐️ 8.0/10

本文提出了 Complex KDA（CKDA），通过将 Kimi Delta Attention（KDA）中对角门的参数范围扩展至\[-1,1\]并将 delta 规则学习率扩展至\[0,2\]来增强其表达能力。理论证明表明，这种扩展使得 CKDA 能够表示任何正交的对角加秩一矩阵，并能追踪 S3、S4 和 A5 群，但无法追踪 S5 群。实验验证了 CKDA 能够成功学习 S3 和 S4 群，在音频续接任务上展现出良好前景，并且在语言建模中能够稳定训练且与标准 KDA 保持竞争力。

reddit · r/MachineLearning · /u/Yossarian\_1234 · 9月22日 10:34

**「背景」** Kimi Delta Attention（KDA）和 Gated Deltanet（GDN）是近期提出的线性注意力机制变体，旨在提升模型的表达能力与计算效率。在标准 KDA 中，全对角门的作用类似于反射操作，但受限于原有的参数范围，无法在单步内完成 2D 旋转变换，这限制了其在特定代数结构和群追踪任务上的理论表达上限。

**「影响」** 对于研究线性 Transformer 和注意力机制的研究者而言，CKDA 提供了一种在保持语言建模竞争力的同时，显著提升模型在正交变换和群追踪等代数任务上表达能力的可行途径。

**标签**: `#machine learning`, `#attention mechanisms`, `#representation theory`, `#linear transformers`, `#deep learning`

---

## 时政综合

<a id="item-world-news-1"></a>
### [Trump’s threat to annihilate Iran to UN general assembly is stunning, even for him](https://www.theguardian.com/us-news/2026/sep/22/donald-trump-unga-speech) ⭐️ 9.0/10

Donald Trump threatened the annihilation of Iran during a UN General Assembly speech, referencing an ongoing war and a major impending decision regarding the country&\#x27;s resistance.

rss · Guardian World · 9月22日 18:23

**标签**: `#UN General Assembly`, `#US-Iran relations`, `#geopolitical escalation`, `#international law`, `#war`

---

