# Horizon 每日速递 - 2026-07-21

> From 20 items, 7 important content pieces were selected

---

1. [Jane Street 的增量计算库：高效重算 DAG](#item-1) ⭐️ 8.0/10
2. [AI 在生成数学反例方面超越人类](#item-2) ⭐️ 8.0/10
3. [Cursor 为智能体集群构建自定义版本控制系统，每秒千次提交](#item-3) ⭐️ 8.0/10
4. [中国开放权重 AI 战略正在获胜](#item-4) ⭐️ 8.0/10
5. [黑客清空罗马尼亚全部土地登记数据库](#item-5) ⭐️ 8.0/10
6. [本·汤普森提议美国立法支持开放 AI 模型](#item-6) ⭐️ 8.0/10
7. [NVIDIA 推出面向设备端 AI 的 Cosmos 3 Edge](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Jane Street 的增量计算库：高效重算 DAG](https://github.com/janestreet/incremental) ⭐️ 8.0/10

Jane Street 发布了 Incremental 库，用于增量计算，当输入变化时能高效地重算有向无环图（DAG）。 该库解决了响应式和函数式编程中的一个基本挑战，使得交易系统和构建工具等性能关键型应用能够增量更新计算，而非从头开始。 Incremental 采用基于 DAG 的模型，节点代表计算，边代表依赖关系，从而在输入变化时仅重算受影响的节点。

hackernews · handfuloflight · Jul 21, 03:50 · [社区讨论](https://news.ycombinator.com/item?id=48987822)

**背景**: 增量计算是一种技术，当输入仅小部分变化时避免重新计算全部结果。它广泛用于构建系统（如 Make、Bazel）、响应式 UI 框架和数据处理管道。Jane Street 是一家量化交易公司，内部开发并使用该库用于高性能应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/janestreet/incremental">janestreet / incremental : A library for incremental computations ...</a></li>
<li><a href="https://blog.janestreet.com/introducing-incremental/">Jane Street Blog - Introducing Incremental</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该库与 UI 框架（Vue、SolidJS、Svelte）中的 JavaScript signals 以及构建系统有相似之处，并提到了 Differential Dataflow 和 DBSP。一位评论者回忆高盛几十年前在工具定价中使用了类似方法。

**标签**: `#incremental computation`, `#reactive programming`, `#functional programming`, `#Jane Street`, `#DAG`

---

<a id="item-2"></a>
## [AI 在生成数学反例方面超越人类](https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/) ⭐️ 8.0/10

Xena 项目的一篇博客文章指出，AI 系统在生成数学猜想反例方面开始超越人类数学家，标志着数学实践正在发生转变。 这一进展可能通过快速证伪错误猜想加速数学发现，节省研究人员多年的无效努力，并可能扩展到理论物理和计算机科学等其他领域。 文章强调，AI 现在能够生成非平凡且令人惊讶的反例，通常使用 Lean 4 定理证明器进行形式验证。社区讨论引用了历史轶事，如张益唐因错误推论而受挫的经历，来说明潜在影响。

hackernews · artninja1988 · Jul 20, 19:03 · [社区讨论](https://news.ycombinator.com/item?id=48983382)

**背景**: 反例是反驳全称命题的具体实例，在数学中通过精炼定义和严格证明发挥关键作用。AI 辅助定理证明，特别是使用 Lean 4，已迅速发展，能够自动生成和验证反例。Xena 项目博客探讨了 AI 与数学的交叉领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Counterexample">Counterexample - Wikipedia</a></li>
<li><a href="https://openreview.net/forum?id=EBa52sye9K">Learning to Disprove: Formal Counterexample Generation with Large Language Models | OpenReview</a></li>
<li><a href="https://www.runlocalai.co/tasks/theorem-proving">Theorem Proving — local AI tasks · RunLocalAI | RunLocalAI</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为这是积极的发展，指出它通过避免徒劳地证明错误猜想而节省时间。一些人将其与物理和计算机科学等其他领域相类比，另一些人则分享了关于未检测到的反例后果的历史轶事，例如张益唐的职业挫折。

**标签**: `#AI`, `#mathematics`, `#research`, `#theorem proving`, `#machine learning`

---

<a id="item-3"></a>
## [Cursor 为智能体集群构建自定义版本控制系统，每秒千次提交](https://cursor.com/blog/agent-swarm-model-economics) ⭐️ 8.0/10

Cursor 从头构建了一个新的版本控制系统（VCS），以支持每秒高达 1,000 次提交的智能体集群，从而实现了仅凭文档用 Rust 从头构建 SQLite 等实验。 这一突破展示了 AI 智能体协调和吞吐量的重大飞跃，可能重塑大规模软件工程任务的自动化方式，并预示着 AI 集群能够自主处理复杂项目的未来。 新 VCS 的构建是因为之前基于 Git 的系统每小时仅能处理 1,000 次提交；自定义 VCS 还充当协调层，使冲突变得可见。从头用 Rust 构建 SQLite 的实验测试了集群处理复杂真实代码生成的能力。

hackernews · jlaneve · Jul 20, 18:06 · [社区讨论](https://news.ycombinator.com/item?id=48982535)

**背景**: 智能体集群是多智能体系统，多个 AI 智能体协作完成任务，通常需要高频通信和版本控制。传统的版本控制系统如 Git 并非为如此高的吞吐量设计，促使 Cursor 构建自定义解决方案。用 Rust 重写 SQLite 的实验值得注意，因为 SQLite 的源代码可能存在于训练数据中，引发了关于记忆与真正推理的疑问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.cursor.com/t/version-control/152397">Version Control - Feature Requests - Cursor - Community Forum</a></li>
<li><a href="https://www.linkedin.com/pulse/agent-swarms-why-ai-agents-moving-from-task-execution-kaushal-verma-wegxc">Agent Swarms : Why AI Agents Are Moving From Task Execution to...</a></li>

</ul>
</details>

**社区讨论**: 评论者对这项工作的实验性质表示兴奋，认为它预示着 AI 工程的未来。一些人质疑用 Rust 重写 SQLite 的任务是否仅仅测试了记忆能力，因为模型可能已经训练过现有的 Rust 重写版本。其他人则争论单智能体与集群方法在工程任务中哪个更有效。

**标签**: `#agent swarms`, `#version control`, `#AI engineering`, `#Cursor`, `#LLM applications`

---

<a id="item-4"></a>
## [中国开放权重 AI 战略正在获胜](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

一篇文章认为，中国的开放权重 AI 模型正在与专有的美国模型竞争中取得进展，引用了初创公司的采用情况和历史类比。 这一转变可能重塑全球 AI 格局，使先进 AI 更易获取，并挑战美国专有模型的主导地位。 文章声称 80%的初创公司使用中国模型，但社区评论质疑这一统计数据，并指出反例，如 Llama 的成功有限。

hackernews · benwerd · Jul 20, 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48979269)

**背景**: 开放权重 AI 模型是指训练后的参数（权重）公开发布，允许任何人下载、运行和微调的模型。这与 GPT-4 等专有模型形成对比，后者仅提供 API 访问。中国通过 DeepSeek 和阿里巴巴等公司积极推广开放权重模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asibiont.com/en/blog/pochemu-strategiya-otkrytykh-vesov-kitaya-pobezhdaet-v-gonke-ii">China 's Open - Weights AI Strategy Is Winning... — ASI Biont Blog</a></li>
<li><a href="https://dev.to/ashraf_chowdury09/is-chinas-open-weights-ai-strategy-actually-winning-10k4">Is China 's Open - Weights AI Strategy Actually... - DEV Community</a></li>
<li><a href="https://www.businessinsider.com/open-source-ai-china-kimi-american-ai-industry-openai-anthropic-2026-7">Americans Are Freaking Out Over China 's Open -Source AI Strategy</a></li>

</ul>
</details>

**社区讨论**: 社区评论对文章的说法表示怀疑，一些人指出企业更看重数据保留和供应商锁定而非开放性。其他人同意，随着硬件成本下降，开放权重模型最终可能占据主导地位。

**标签**: `#AI`, `#open-source`, `#China`, `#technology strategy`, `#machine learning`

---

<a id="item-5"></a>
## [黑客清空罗马尼亚全部土地登记数据库](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

一名黑客在勒索未遂后删除了罗马尼亚的整个土地登记数据库，导致全国房地产市场瘫痪，所有房产交易暂停。该机构拥有离线备份，并正在将应用程序迁移至罗马尼亚政府云以恢复数据。 此次攻击瘫痪了关键国家基础设施，导致公证人无法认证销售或登记抵押贷款，带来严重的社会和经济后果。它凸显了离线备份的重要性以及政府系统面对勒索软件和勒索攻击的脆弱性。 黑客被确认为来自阿尔及利亚奥兰的 Zakaria Mahdjoub，声称已删除备份，但该机构拥有离线副本。向政府云的迁移由特别电信服务局（STS）协调，预计于 7 月 22 日前完成。

hackernews · speckx · Jul 20, 13:28 · [社区讨论](https://news.ycombinator.com/item?id=48978605)

**背景**: 罗马尼亚土地登记是一个国家财产数据库，记录所有权、边界和权利主张，是房地产交易的法律基础。离线备份是独立于主系统存储的副本，确保即使在线备份受损也能恢复数据。政府云基础设施是指公共机构用于托管应用程序和数据的集中式安全云服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/security/hacker-deletes-romanian-land-registry-database/">Hacker deletes country’s entire land registry database ... | Cybernews</a></li>
<li><a href="https://outsourcing-today.ro/?p=14259">Romania’s Government Cloud Takes Off: Endava Romania Signs...</a></li>
<li><a href="https://theromanianlawyers.com/the-land-registry-process-in-romania-a-comprehensive-overview/">The Land Registry Process in Romania : A Comprehensive Overview</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，如果没有离线备份，将引发社会混乱；一些罗马尼亚消息来源将此次入侵归咎于政府 IT 合同中的腐败。黑客的身份以及阿尔及利亚与罗马尼亚的引渡条约也引发了讨论。

**标签**: `#cybersecurity`, `#data breach`, `#backup`, `#critical infrastructure`, `#hacking`

---

<a id="item-6"></a>
## [本·汤普森提议美国立法支持开放 AI 模型](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

本·汤普森提议美国通过一项法律，明确将训练数据收集视为合理使用，并禁止禁止蒸馏的服务条款，以帮助美国开放模型与中国模型竞争。他还指出，阿里巴巴以开放权重发布了 Qwen 3.8 Max，可能受到习近平鼓励开源的讲话影响。 该提案解决了 AI 实验室在未经许可数据上训练却禁止蒸馏的虚伪问题，并可能通过允许美国开放模型利用蒸馏技术来重塑中美 AI 竞争格局。如果实施，将为开源 AI 开发创造更公平的竞争环境。 Qwen 3.8 Max 是一个 2.4 万亿参数的模型，几乎与 Kimi K3 的 2.8 万亿参数相当。汤普森认为，阻止蒸馏几乎不可能，因为它只是查询 API，因此美国应该将其合法化并促进创新。

rss · Simon Willison · Jul 20, 17:09

**背景**: 模型蒸馏是一种让较小模型从较大模型输出中学习的技术，常用于创建高效模型。美国目前对使用受版权数据训练的版权状态存在争议，AI 公司主张合理使用。像 Qwen 这样的中国 AI 模型以开放权重发布，而一些美国实验室通过服务条款限制蒸馏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.skadden.com/insights/publications/2025/05/copyright-office-report">Copyright Office Weighs In on AI Training and Fair Use | Skadden, Arps, Slate, Meagher & Flom LLP</a></li>
<li><a href="https://lib.guides.umd.edu/ai-scholarly-communications/fair-use">Fair Use and AI Training Data - Artificial Intelligence (AI) and Scholarly Communications - Research Guides at University of Maryland Libraries</a></li>

</ul>
</details>

**社区讨论**: 文章未提供评论，但 Simon Willison 博客及相关来源的讨论可能包括对汤普森提案的支持及其可行性的辩论。没有直接的社区评论。

**标签**: `#AI policy`, `#open models`, `#distillation`, `#copyright`, `#US-China competition`

---

<a id="item-7"></a>
## [NVIDIA 推出面向设备端 AI 的 Cosmos 3 Edge](https://huggingface.co/blog/nvidia/cosmos3edge) ⭐️ 8.0/10

NVIDIA 发布了 Cosmos 3 Edge，这是一个基于 Nemotron 构建的紧凑型 40 亿参数开放世界模型，专为在 Jetson 等边缘设备上高效部署而设计。 该模型无需依赖云端即可在边缘设备上直接实现实时视觉推理和机器人动作生成，推动了机器人和自主系统的设备端 AI 发展。 Cosmos 3 Edge 既可作为小型视觉语言模型（VLM），也可作为后训练的世界动作模型（WAM），且可在单个 GPU 上进行推理。

rss · Hugging Face Blog · Jul 20, 15:58

**背景**: 边缘 AI 是指在本地设备而非云端部署 AI 推理，从而降低延迟并提升隐私性。NVIDIA 的 Jetson 平台专为边缘计算设计，而 Cosmos 3 Edge 则针对此类硬件进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/cosmos3edge">Introducing Cosmos 3 Edge</a></li>
<li><a href="https://huggingface.co/nvidia/Cosmos3-Edge">nvidia/Cosmos3-Edge · Hugging Face</a></li>
<li><a href="https://kie.ai/blog/what-is-cosmos-3-edge">What Is Cosmos 3 Edge? NVIDIA's 4B Robot Model</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#edge AI`, `#small language model`, `#on-device AI`

---

