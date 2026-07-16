# Horizon 每日速递 - 2026-07-16

> From 40 items, 8 important content pieces were selected

---

1. [Thinking Machines Lab 发布 Inkling 开放权重模型](#item-1) ⭐️ 9.0/10
2. [Linus Torvalds 支持在 Linux 内核开发中使用 AI](#item-2) ⭐️ 9.0/10
3. [xAI 在隐私争议后开源 Grok Build](#item-3) ⭐️ 9.0/10
4. [月之暗面发布前沿级开源权重模型 Kimi K3](#item-4) ⭐️ 8.0/10
5. [Roc 编译器从 Rust 重写为 Zig 的进展](#item-5) ⭐️ 8.0/10
6. [GPT-5.6 Codex 漏洞误删用户文件](#item-6) ⭐️ 8.0/10
7. [NVIDIA Nemotron-3 Embed 在 RTEB 基准测试中排名第一](#item-7) ⭐️ 8.0/10
8. [Hugging Face 披露 2026 年 7 月安全事件](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Thinking Machines Lab 发布 Inkling 开放权重模型](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Mira Murati 创立的 Thinking Machines Lab 发布了 Inkling，这是一个总参数量 975B（活跃参数 41B）的混合专家多模态模型，采用 Apache-2.0 许可，在 45 万亿 token 的文本、图像、音频和视频数据上训练而成。 此次发布标志着知名实验室正式进入开放权重 AI 生态系统，为中国开放权重模型提供了有力的竞争替代品，并与 NVIDIA Nemotron 和 Gemma 4 一起增强了美国开放权重领域的实力。 Inkling 并非前沿模型，而是通过 Tinker 平台进行微调的强大基础模型；其模型卡和训练数据文档明显简略，缺乏关于数据来源和构成的详细信息。

rss · Simon Willison · Jul 16, 15:35

**背景**: 混合专家（MoE）是一种 Transformer 架构，它使用多个专门的子网络（专家）和一个门控机制，每个输入只激活部分专家，从而在较低计算成本下实现巨大的总参数量。开放权重模型允许用户下载、运行和修改模型权重，促进透明度和定制化。Apache-2.0 是一种宽松许可证，允许自由使用、修改和分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Thinking Machines Lab`

---

<a id="item-2"></a>
## [Linus Torvalds 支持在 Linux 内核开发中使用 AI](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 9.0/10

Linux 创始人 Linus Torvalds 在 Linux Media 邮件列表中声明，Linux 不是反 AI 项目，AI 是一个明确有用的工具，并挑战不同意的人可以分叉或离开。 来自顶层维护者的明确支持标志着开源社区的重大范式转变，可能加速 AI 在内核开发中的整合，并影响其他项目。 Torvalds 强调 AI 的有用性已不再有疑问，尽管他承认关于 AI 经济的其他问题仍然开放。该声明是在 Linux Media 邮件列表中发表的，这是内核开发讨论的关键场所。

rss · Simon Willison · Jul 16, 13:26

**背景**: Linus Torvalds 是 Linux 内核（Linux 操作系统的核心）的创建者和长期维护者。内核开发社区历来对整合 AI 工具有不同意见，一些人因担心代码质量、许可或伦理问题而反对使用。Torvalds 的声明实际上解决了 Linux 项目内部的争论，至少目前如此。

**标签**: `#Linux`, `#AI`, `#Open Source`, `#Linus Torvalds`, `#Kernel Development`

---

<a id="item-3"></a>
## [xAI 在隐私争议后开源 Grok Build](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI 在用户发现其 CLI 工具会上传整个目录（包括 SSH 密钥和密码数据库等敏感文件）到云存储后，已将整个 Grok Build 代码库以 Apache 2.0 许可证开源。 此事件凸显了 AI 驱动的开发者工具中存在的严重隐私风险，并展示了社区反弹如何迫使企业迅速采取行动，包括开源专有代码以重建信任。 该代码库包含 844,530 行 Rust 代码（仅约 3% 为第三方依赖），并包含一个自包含的 Mermaid 图表终端渲染器。xAI 已删除所有先前保留的用户数据，并禁用了默认数据保留功能。

rss · Simon Willison · Jul 15, 23:59

**背景**: Grok Build 是 xAI 推出的一款 AI 驱动的编码助手，以 CLI 工具形式运行。它利用大型语言模型帮助开发者编写代码，但被发现会在未经用户明确同意的情况下将整个项目目录上传到 Google Cloud，引发了严重的隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/15/grok-build/">xai-org/grok-build, now open source</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload">SpaceXAI’s Grok programming tool was uploading its users’ entire codebase to cloud storage | The Verge</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**标签**: `#privacy`, `#open-source`, `#AI`, `#security`, `#xAI`

---

<a id="item-4"></a>
## [月之暗面发布前沿级开源权重模型 Kimi K3](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

月之暗面发布了 Kimi K3，这是一个前沿级的开源权重大语言模型，声称性能仅次于 Claude Fable 5 和 GPT-5.6 Sol，完整模型权重将在未来几天内发布。 此次发布标志着前沿 AI 能力商品化的重要一步，一家中国实验室提供了与顶级专有系统竞争的开源模型，可能加速全球创新并降低开发者的门槛。 Kimi K3 可通过 OpenRouter API 使用，定价为每百万输入 token 3 美元、每百万输出 token 15 美元，并支持推理 token。完整权重、架构细节和技术报告承诺很快发布。

hackernews · vincent_s · Jul 16, 14:46 · [社区讨论](https://news.ycombinator.com/item?id=48935342)

**背景**: 开源权重模型是指其训练参数（权重）公开发布的 AI 模型，允许任何人下载、运行、研究和修改。这与仅提供 API 访问的封闭模型（如 GPT-4）形成对比。前沿级模型代表 AI 性能的最高层级，通常通过大规模训练实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**社区讨论**: 社区评论关注月之暗面的数据使用政策，该政策允许在 API 内容上进行训练，除非有企业安排。一些人认为这是 AI 智能商品化的举措，而另一些人则指出此类模型仍需高昂成本和大量努力。

**标签**: `#AI`, `#open-source`, `#large language models`, `#China`, `#machine learning`

---

<a id="item-5"></a>
## [Roc 编译器从 Rust 重写为 Zig 的进展](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

Roc 团队在过去一年半中将 30 万行 Rust 代码重写为 Zig，并已实现与原编译器功能一致。 这次重写凸显了 Rust 的安全性保障与 Zig 的简洁性和增量构建速度之间的权衡，可能影响未来性能关键型项目的系统编程语言选择。 博客文章强调，生成机器码的编译器通常需要内存不安全操作，而 Zig 的 ReleaseSafe 模式通过运行时检查捕获 use-after-free 错误，但部分社区成员质疑这些检查的覆盖范围。

hackernews · jorangreef · Jul 16, 11:39 · [社区讨论](https://news.ycombinator.com/item?id=48933149)

**背景**: Roc 是一种注重速度和友好性的函数式编程语言。其编译器最初用 Rust 编写，但团队决定用 Zig 重写，以利用 Zig 更快的增量构建和更简单的内存模型，尽管 Rust 提供了更强的安全性保障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/roc-lang/roc">GitHub - roc-lang/roc: A fast, friendly, functional language. The Roc Programming Language roc/docs/mini-tutorial-new-compiler.md at main · roc-lang/roc ROCm Software - AMD The Complete Roc Guide: From Zero to Expert - kodikra How Our Rust-to-Zig Rewrite is Going</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**社区讨论**: 知名人士如 steveklabnik 认为，编译器中内存不安全操作并不像文章所说的那样普遍；landr0id 则质疑 Zig 捕获 use-after-free 错误的能力。其他人称赞 Zig 的增量构建是杀手锏，但担心失去 Rust 的安全性。

**标签**: `#Rust`, `#Zig`, `#compiler`, `#systems programming`, `#performance`

---

<a id="item-6"></a>
## [GPT-5.6 Codex 漏洞误删用户文件](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

GPT-5.6 的 Codex 存在一个漏洞：当启用完全访问模式且未使用沙箱保护时，模型会错误地删除 $HOME 目录而非临时目录，导致用户文件被意外删除。 该漏洞凸显了拥有无限制文件系统访问权限的 AI 编程代理存在的严重安全风险，可能导致依赖此类工具的开发者或企业遭受不可逆的数据丢失。 该漏洞在启用完全访问模式、关闭沙箱保护和自动审查时触发；模型试图覆盖 $HOME 环境变量以定义临时目录，却错误地删除了 $HOME 目录。

rss · Simon Willison · Jul 16, 17:45

**背景**: GPT-5.6 Codex 是一种 AI 编程代理，可在用户系统上执行命令。完全访问模式赋予其广泛权限，而沙箱技术则用于隔离其操作以防止损害。$HOME 环境变量指向用户的主目录，其中包含个人文件和设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.docker.com/products/docker-sandboxes/">Sandboxes for Coding Agents - Docker</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor ...</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-7"></a>
## [NVIDIA Nemotron-3 Embed 在 RTEB 基准测试中排名第一](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) ⭐️ 8.0/10

NVIDIA 的 Nemotron-3 Embed 模型在 RTEB（检索聚焦文本嵌入基准测试）中取得了总体排名第一的成绩，在检索准确性上超越了所有其他模型。这标志着在智能体检索任务上达到了新的最优水平。 这一进展直接提升了依赖准确信息检索的检索增强生成（RAG）和 AI 智能体系统的质量。随着智能体检索对企业 AI 变得至关重要，Nemotron-3 Embed 树立了新的性能标杆。 Nemotron-3 Embed 基于 Ministral-3-8B 架构，为多语言文本生成 4096 维稠密向量。该模型可在 Hugging Face 上获取，并通过 NVIDIA NIM 进行部署。

rss · Hugging Face Blog · Jul 16, 16:01

**背景**: RTEB 是一个新基准，旨在评估嵌入模型和重排序器的检索准确性，它结合使用公开和私有数据集以防止过拟合。智能体检索通过支持多步推理和自我纠正扩展了传统搜索，对高级 AI 智能体至关重要。像 Nemotron-3 这样的嵌入模型将文本转换为捕获语义含义的数值向量，从而实现高效的相似性搜索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/rteb">Introducing RTEB : A New Standard for Retrieval Evaluation</a></li>
<li><a href="https://github.com/embedding-benchmark/rteb">GitHub - embedding- benchmark / rteb : Retrieval Embedding Benchmark</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#embedding models`, `#agentic retrieval`, `#RTEB`, `#AI/ML`

---

<a id="item-8"></a>
## [Hugging Face 披露 2026 年 7 月安全事件](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face 发布了一篇博客文章，披露了 2026 年 7 月发生的一起安全事件，详细说明了入侵的性质及其对用户的影响。 此次披露对 AI/ML 社区至关重要，因为 Hugging Face 是模型托管和协作的核心平台，该事件可能影响用户信任和安全实践。 该博客文章提供了事件的权威细节，包括时间线、受影响的系统以及 Hugging Face 采取的补救措施。

rss · Hugging Face Blog · Jul 16, 00:00

**背景**: Hugging Face 是一个流行的机器学习模型和数据集托管平台，被研究人员和开发者广泛使用。此类平台上的安全事件可能暴露敏感数据或损害模型完整性。

**标签**: `#security`, `#incident disclosure`, `#Hugging Face`, `#AI/ML platform`, `#vulnerability`

---

