# Horizon 每日速递 - 2026-08-01

> From 17 items, 8 important content pieces were selected

---

1. [OpenAI 称内部 Astra 模型以每个不到 2000 美元解决十个十年未解数学难题](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4-Flash-0731：304B 开源权重模型，智能体能力大幅提升](#item-2) ⭐️ 9.0/10
3. [无状态 MCP 2.0 重燃热情，催生新工具](#item-3) ⭐️ 9.0/10
4. [《64 位汇编的艺术》新版发布引发热议](#item-4) ⭐️ 8.0/10
5. [NetBSD 11.0 发布，带来 MicroVM 内核与防火墙增强](#item-5) ⭐️ 8.0/10
6. [Ripgrep 的 musl 构建在大规模搜索中偶发段错误](#item-6) ⭐️ 8.0/10
7. [加拿大签署联合国网络犯罪公约，引发隐私担忧](#item-7) ⭐️ 8.0/10
8. [硅谷创始人绞肉机：一个警示故事](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 称内部 Astra 模型以每个不到 2000 美元解决十个十年未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 9.0/10

2026 年 8 月 1 日，OpenAI 宣布其下一代主要模型系列 Astra 的内部版本解决了数学与理论计算机科学中十个长期悬而未决的问题。该公司表示，按 GPT-5.6 Sol 代币价格计算，每个问题的解决成本不到 2000 美元，并发布了 Lean 4 形式化证明及相关论文。 这标志着 AI 推理能力的显著跃升，解决了至少十年未有核心进展的问题。它可能加速数学研究，并推动该领域走向陶哲轩所设想的“大数学”愿景——由人类负责创造性部分，AI 承担大量技术性工作。 这些结果已在 GitHub 仓库 openai/ten-proofs 中以 Lean 4 形式化，并附有一篇论文和一份 LLM 生成的 PDF，后者根据未公开的推理轨迹重建了证明的形成过程。Simon Willison 指出，OpenAI 没有报告有多少问题花了 2000 美元却未解决，因此只公布十个成功案例可能高估了该模型的实际成功率。

rss · Simon Willison · Aug 1, 20:34

**背景**: Lean 4 是一种交互式定理证明器，让数学家可以编写机器可验证的证明，使验证变得算法化，而不再依赖人工审查。OpenAI 的这次公告首次正式将 Astra 命名为其下一代主要模型系列。此前 Anthropic 的 Claude Mythos Preview 发现了密码学弱点，显示出前沿模型被应用于艰难技术研究的更广泛趋势。陶哲轩将 AI 视为“大数学”的催化剂，认为未来将出现人机协作的大规模研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its "next major model" Astra by dropping ten ...</a></li>
<li><a href="https://www.bitsminds.com/news/openai-astra-ten-open-math-problems-lean-proofs-2026">OpenAI Names Its Next Model Family Astra — and Says It Solved ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#problem-solving`

---

<a id="item-2"></a>
## [DeepSeek V4-Flash-0731：304B 开源权重模型，智能体能力大幅提升](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 9.0/10

DeepSeek 于 2026 年 7 月 31 日发布了 deepseek-ai/DeepSeek-V4-Flash-0731，这是一款报告参数规模为 304B（Hugging Face 上 167GB）的开源权重模型，宣称“智能体能力大幅增强”。其定价为每百万输入 token 0.14 美元、每百万输出 token 0.27 美元。 该模型在 Artificial Analysis 的智能指数（Intelligence Index）上超越 MiniMax M3（428B），但成本低得多，可能是目前单位智能性价比最高的开源权重模型。这标志着对闭源前沿模型的持续竞争压力，尤其是对成本敏感的高并发智能体工作负载。 Simon Willison 发现，通过 OpenRouter 将推理级别调高（'reasoning_effort high'）后，图像生成质量明显改善，而默认级别生成的自行车形象扭曲。需要说明的是，304B 参数来自 Willison 的博客；其他来源称该 MoE 模型总参数为 284B，每 token 激活 13B，上下文长度 100 万 token，且 API 已原生支持 Responses API 格式并适配 Codex。

rss · Simon Willison · Jul 31, 23:59

**背景**: DeepSeek 是一家以发布具有竞争力的开源权重模型而知名的中国 AI 实验室。V4-Flash 是 DeepSeek V4 系列中专攻效率的模型，采用混合专家（MoE）架构，每个 token 只激活一小部分参数。Artificial Analysis 智能指数是一个综合基准，汇总了数学、科学、编程和推理等九个高难度评测，用于横向比较模型智能水平。此次发布延续了中国开源权重模型在性能上追赶西方前沿实验室、同时在价格上大幅压低成本的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/deepseek-v4-flash-official-release">DeepSeek V4 Flash: Official Release, Explained</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index</a></li>
<li><a href="https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/">DeepSeek Upgrades DeepSeek-V4-Flash-0731 with Major Agentic ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#AI`, `#open-weight`, `#machine learning`

---

<a id="item-3"></a>
## [无状态 MCP 2.0 重燃热情，催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 9.0/10

2026 年 7 月 28 日，Anthropic 发布了无状态 MCP 2.0 规范（即 2026-07-28 Model Context Protocol 规范），这是一次移除会话状态的重要更新。Simon Willison 将周二称为“无状态 MCP 日”，并为此构建了三个新工具，包括 mcp-explorer 和 datasette-mcp。 这次更新大幅降低了实现 MCP 客户端和服务器的复杂度，使该协议对可扩展的 Web 应用以及运行在笔记本电脑上的小型模型更具吸引力。它也让曾转向 Anthropic Skills 的开发者重新关注 MCP，巩固了 MCP 作为 AI 代理工具核心标准的地位。 新的无状态方式使用单个 HTTP 请求，通过 "MCP-Protocol-Version" 和 "Mcp-Method" 等头部传递信息，无需初始化握手和服务端会话 ID。这使得工具更易于审计和控制，也更适合水平扩展的后端，因为请求可以被路由到任意机器。

rss · Simon Willison · Jul 31, 23:13

**背景**: Model Context Protocol（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在规范 AI 系统连接外部工具和数据源的方式。最初的有状态 MCP 需要两步 HTTP 交换——先初始化会话获取 Mcp-Session-Id，再发送实际的工具调用——这增加了服务端状态管理的开销。新的 2026-07-28 规范使协议变为无状态，每个请求都包含全部所需的上下文，从而提高了可靠性和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#MCP`, `#Model Context Protocol`, `#Anthropic`, `#AI agents`, `#stateless`

---

<a id="item-4"></a>
## [《64 位汇编的艺术》新版发布引发热议](https://nostarch.com/art-64-bit-assembly-v2) ⭐️ 8.0/10

No Starch Press 宣布推出《The Art of 64-bit Assembly》第二版，这是一本介绍使用 MASM 在 Windows 上进行 x64 汇编编程的综合性书籍。这一消息引发了关于汇编语言是否仍然重要以及 AI 生成文本在书籍营销中作用的讨论。 该书的发布重新引发了关于在高级语言和 AI 辅助开发时代汇编语言是否仍然重要的长期争论。社区的反映也凸显了人们对技术出版物中 AI 生成内容日益增长的不安。 这本书有近 800 页，专门介绍使用 MASM 的 x64 Windows 汇编，一些评论者认为这个书名具有误导性。据报道，开场营销文案鼓励读者向 AI 寻求帮助，这引起了那些希望看到作者自己解释的人的批评。

hackernews · 0x54MUR41 · Aug 1, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49134599)

**背景**: 汇编语言是一种直接对应 CPU 指令集的低级编程语言。x64 是大多数现代台式机和服务器处理器使用的 64 位指令集架构，而 MASM 是微软用于 Windows 开发的汇编器。这本书旨在提供汇编编程的全面教育，虽然许多人认为这一主题已经过时，但它对于底层系统编程和性能关键代码仍然具有现实意义。

**社区讨论**: 社区反应不一：有人称赞这本书的雄心以及学习汇编语言仍有价值，也有人批评营销文案、AI 生成文本的使用以及局限于 Windows/MASM。还有评论者询问是否有 Linux 等效书籍，并比较了 GAS 和 MASM 的功能集。

**标签**: `#assembly`, `#programming`, `#book`, `#low-level`, `#hackernews`

---

<a id="item-5"></a>
## [NetBSD 11.0 发布，带来 MicroVM 内核与防火墙增强](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 8.0/10

NetBSD 11.0 已正式发布，为 x86 引入了新的 MICROVM 内核，并对 NPF 防火墙进行了重要改进，包括二层过滤和用户/组过滤。这是一个主要版本更新，面向这个可移植的类 Unix 操作系统。 MICROVM 内核使 NetBSD 能在 QEMU 中约 10 毫秒内启动，使其成为轻量级云和边缘工作负载的有力候选。NPF 的增强巩固了 NetBSD 作为安全、灵活防火墙平台的地位，对嵌入式和服务端部署都有意义。 新的 MICROVM 内核同时支持 i386 和 amd64，利用 PVH 引导、VirtIO MMIO 以及多项内核优化；而 QEMU 的 microvm 机型不提供 PCI 总线和支持 ACPI。发布版还包含硬件支持更新，NPF 防火墙则新增了二层过滤和用户/组过滤能力。

hackernews · jaypatelani · Aug 1, 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49136736)

**背景**: NetBSD 是一个高度可移植的开源类 Unix 操作系统，以支持众多硬件平台著称。MICROVM 内核专为 QEMU 的 microvm 机型设计，旨在优化虚拟化环境中的启动时间和体积。NPF 是 NetBSD 的有状态包过滤器，类似于 Linux 的 iptables 或 OpenBSD 的 PF，由 NetBSD 项目开发维护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.netbsd.org/releases/formal-11/NetBSD-11.0.html">Announcing NetBSD 11.0 RC7 (July 21, 2026)</a></li>
<li><a href="https://wiki.netbsd.org/users/imil/microvm/">microvm</a></li>
<li><a href="https://www.phoronix.com/news/smolBSD">smolBSD Builds On The NetBSD-MicroVM Kernel For Booting To Service VMs In Milliseconds - Phoronix</a></li>

</ul>
</details>

**社区讨论**: 评论者对 BSD 相比 Linux 的现状表示好奇，询问谁在使用它们，以及在功能和安全性方面如何比较。其他人则称赞了 MICROVM 内核约 10 毫秒的启动时间和 NPF 的新过滤功能；还有评论者指出，发布公告对已知未解决问题所采取的谦逊语气出人意料。

**标签**: `#NetBSD`, `#BSD`, `#operating system`, `#release`, `#open-source`

---

<a id="item-6"></a>
## [Ripgrep 的 musl 构建在大规模搜索中偶发段错误](https://github.com/BurntSushi/ripgrep/issues/3494) ⭐️ 8.0/10

GitHub 上的一个 bug 报告（ripgrep issue #3494）显示，使用 musl libc 构建的 ripgrep 二进制文件在非常大的搜索过程中可能会偶尔出现段错误。该报告引发了深入的技术讨论，将崩溃与内核补丁和 musl 的内存分配器行为联系起来。 Ripgrep 是一款广泛使用的搜索工具，尤其在 Linux 和用 musl 构建的静态二进制文件中；段错误 bug 会削弱 Alpine Linux 或其他基于 musl 的系统上用户的可靠性。它还凸显了 musl 默认分配器在多线程环境下的更广泛性能问题，影响面远超 ripgrep。 讨论中引用了一个内核补丁和一个详细的分析仓库（dfoxfranke/ripgrep-3494-analysis）来探究根本原因。评论者指出，musl 的 mallocng 分配器在线程竞争下表现不佳，并建议用 mimalloc 等性能更好的分配器替换默认分配器。

hackernews · throwaway2037 · Aug 1, 12:34 · [社区讨论](https://news.ycombinator.com/item?id=49133889)

**背景**: Ripgrep 是一个命令行搜索工具，以递归方式在目录中搜索正则表达式模式，以速度快著称。musl 是一个轻量级 C 库，常用于 Alpine Linux 和静态二进制文件，是 glibc 的替代品。musl 的默认内存分配器（mallocng）设计目标是简单和低内存占用，但在高并发多线程下扩展性不佳。对于大型搜索，ripgrep 会使用多个线程，这可能会暴露 musl 分配器中的竞争问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.musl-libc.org/intro.html">musl - Introduction</a></li>
<li><a href="https://www.linkedin.com/pulse/testing-alternative-c-memory-allocators-pt-2-musl-mystery-gomes">Testing Alternative C Memory Allocators Pt 2: The MUSL mystery</a></li>
<li><a href="https://www.openeuler.org/en/blog/20230529-Musl/20230529-Musl.html">Adapting musl libc for openEuler Embedded | openEuler</a></li>

</ul>
</details>

**社区讨论**: 评论者通常是在分享见解而非争论：一位指出，替换 musl 默认分配器通常会被避免，但对像 ripgrep 这样注重速度的应用可能合适。另一位警告说，在 HPC 上针对大型集群文件系统运行 ripgrep 会产生过多的小 I/O，应重新设计工作流。还有用户询问为什么该 bug 只在 musl 下触发，另一些人则链接了那个被误认为人类所写的 AI 生成分析。

**标签**: `#ripgrep`, `#musl`, `#segfault`, `#bug`, `#performance`

---

<a id="item-7"></a>
## [加拿大签署联合国网络犯罪公约，引发隐私担忧](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/) ⭐️ 8.0/10

加拿大悄然签署了《联合国网络犯罪公约》，批评者称此举等同于支持一项削弱隐私权的监控条约。迈克尔·盖斯特（Michael Geist）报道了这一消息，并指出签署过程缺乏公开讨论。 该事件意义重大，因为该公约可能重塑国际数字监控和执法合作，进而侵蚀加拿大公民的隐私保护。它也反映出各国政府在公民自由受到关切的情况下仍签署宽泛网络犯罪条约的趋势。 《联合国网络犯罪公约》已吸引七十多个签署方，但仅签署而未批准时对国家影响有限。批评者认为公约条款偏重监控而忽视隐私，支持者则强调其在打击网络犯罪中的作用。

hackernews · iamnothere · Aug 1, 14:19 · [社区讨论](https://news.ycombinator.com/item?id=49134694)

**背景**: 《联合国网络犯罪公约》是一项旨在加强打击网络犯罪国际合作的条约，包括促进跨境获取电子证据。该公约受到隐私倡导者的批评，他们认为广泛的数据收集和共享权力可能助长国家监控。各国通常先进行签署以表明意向，随后通过批准使条约在国内具有法律约束力。

**社区讨论**: 评论指出，包括澳大利亚、欧盟和英国在内的多个国家也已签署该公约，但真正重要的是批准程序。有评论者称赞迈克尔·盖斯特在隐私问题上二十年的工作，另有评论者指出加拿大通常倾向于签署大多数联合国条约，表明这只是例行公事。还有人对此问题上政治信号的真实性表示怀疑。

**标签**: `#cybercrime`, `#surveillance`, `#privacy`, `#Canada`, `#UN treaty`

---

<a id="item-8"></a>
## [硅谷创始人绞肉机：一个警示故事](https://zaksa.zip/blog/silicon-valley-founder-meat-grinder/) ⭐️ 8.0/10

这篇文章讲述了硅谷创始人吉姆的故事，他沉迷于追求财富和创业生活方式，最终导致与未婚妻分手并精神崩溃。文章批评了创业文化从打造有意义的产品转向追逐金钱的转变。 这篇文章揭示了硅谷创业文化中阴暗的一面，即对金钱和地位的痴迷可能造成严重的个人代价。它与行业内对倦怠、心理健康以及科技创业真实性的广泛担忧产生了共鸣。 叙述跟随吉姆进入湾区时对创业充满热情，却陷入财务鲁莽、沉迷吸毒的“创始人派对”和群体性行为的生活方式，最终导致个人崩溃。作者还把他家酿啤酒的爱好当作财务不负责任的例子，评论者对此感到讽刺。

hackernews · Kaizeras · Aug 1, 20:20 · [社区讨论](https://news.ycombinator.com/item?id=49138045)

**背景**: 硅谷以其高风险、高回报的创业生态而闻名，风险投资和巨额退出的承诺吸引了雄心勃勃的创业者。批评者认为，随着时间推移，这种文化已从打造创新产品转向追逐财富和地位，而加密货币热潮和一批渴望快速致富的人加剧了这一趋势。如今，“创始人”这一身份承载着人们对极端成功和极端牺牲的双重期待。

**社区讨论**: 评论者反应不一：egonschiele 感叹科技文化过于以金钱为中心，并指出比特币财富的影响；lmeyerov 则用一个通过坚持做到年收入千万美元的故事进行反驳。Aurornis 批评湾区有很多人“扮演”聪明创始人却鲜有产出，FinnLobsien 认为问题在于想要“富有创始人”的身份而非做实事。Carrok 则觉得家酿啤酒的例子很滑稽。

**标签**: `#startup-culture`, `#silicon-valley`, `#founder-struggles`, `#tech-critique`, `#venture-capital`

---

