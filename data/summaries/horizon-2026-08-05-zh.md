# Horizon 每日速递 - 2026-08-05

> 从 152 条内容中筛选出 7 条重要资讯。

---

**科技新闻**
1. [感谢联邦快递：我们为何不断被钓鱼](#item-tech-news-1) ⭐️ 8.0/10
2. [单块 MI300X 运行 DeepSeek V4 Flash](#item-tech-news-2) ⭐️ 8.0/10
3. [Keyv 及关联 npm 包遭 Shai-Hulud 供应链攻击](#item-tech-news-3) ⭐️ 8.0/10
4. [Xbox 宕机导致光盘游戏无法游玩，引发数字所有权争论](#item-tech-news-4) ⭐️ 8.0/10
5. [为自我改进 AI agent 设计 harness 的工程实践](#item-tech-news-5) ⭐️ 8.0/10
6. [MiniMax-H3 的 MLX 移植：在 Apple Silicon 上本地运行视频生成](#item-tech-news-6) ⭐️ 8.0/10
7. [华为首席科学家警告英伟达式扩展将触及物理极限](#item-tech-news-7) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [感谢联邦快递：我们为何不断被钓鱼](https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/) ⭐️ 8.0/10

Troy Hunt 在 2024 年的文章《Thanks FedEx, This Is Why We Keep Getting Phished》中指出，联邦快递等合法企业的通知邮件在形式上与钓鱼邮件高度相似，削弱了用户的安全意识和培训效果。具体例子包括：有用户收到发自 FedEx 个人邮箱、带有 PDF 附件的海关通知，原本以为是诈骗，经人工客服确认才是官方消息；谷歌的存储容量提醒邮件使用 c.gle 短域名，普通用户难以验证其真实性。文章认为，这类合法通信反而让用户更难分辨真正的钓鱼攻击，并引用 ACMA 关于已拦截 3.36 亿条诈骗短信的数据作为背景。

hackernews · stymaar · 8月4日 21:09 · [社区讨论](https://news.ycombinator.com/item?id=49175192)

**「背景」** 这则内容围绕安全研究员 Troy Hunt 在 2024 年 2 月的一篇文章，他举出 FedEx 的合法短信和电子邮件在形式上与常见钓鱼信息高度相似，包含多个通常被视为诈骗警号的痕迹（如大小写不规范和可疑链接）。这造成一种安全悖论：安全培训要求用户警惕这些危险信号，但合法企业通信却经常具备这些特征，削弱了用户的警惕性，并可能使他们对真正的钓鱼攻击失去判断力。

**「影响」** 对普通用户和依赖邮件特征识别诈骗的安全培训而言，企业官方通知与钓鱼邮件过于相似，会直接削弱用户对警告的信任，增加落入真实钓鱼陷阱的风险。

**「社区讨论」** 评论者提供了多则亲历例证：有人收到 FedEx 个人邮箱发来的 PDF 海关通知，最终确认属实；有人收到看似合法的 Google 存储提醒，但链接域名 c.gle 难以验证；还有人指出 IRS 电话语音系统与诈骗电话使用同一文本转语音系统，且新兴通用顶级域名泛滥也让普通人更难辨别钓鱼链接。整体共识是企业自身在采用与攻击者类似的沟通方式，加剧了识别难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/">Troy Hunt: Thanks FedEx, This is Why we Keep Getting Phished</a></li>
<li><a href="https://www.linkedin.com/posts/troyhunt_thanks-fedex-this-is-why-we-keep-getting-activity-7166717646028165120-8nOs">Troy Hunt on LinkedIn: Thanks FedEx, This is Why we Keep Getting Phished | 11 comments</a></li>

</ul>
</details>

**标签**: `#phishing`, `#security`, `#email`, `#social engineering`, `#infosec`

---

<a id="item-tech-news-2"></a>
### [单块 MI300X 运行 DeepSeek V4 Flash](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 8.0/10

开发者发布了一项在单块 AMD MI300X 上运行 DeepSeek V4 Flash 的详细方案，通过原生 MXFP4 量化和内存优化，实现了每秒超过 150 token 的推理吞吐，但将上下文窗口从原有的 1M 缩短至 256K。该模型是一个大型 MoE 模型，这种取舍使单 GPU 部署变得实际可行。不过，MI300X 是 OAM 模块，无法单独购买，通常只能通过约 25 万欧元的 8 卡整机或云租赁服务获取。社区指出，MI350P PCIe 卡虽然内存更少（144GB），但由于该模型原生采用 MXFP4 量化，也能运行同样模型。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**「背景」** DeepSeek V4 Flash（DeepSeek-V4-Flash-0731）是 DeepSeek 的大型混合专家（MoE）模型，其配置中声明 \`expert\_dtype=fp4\`，路由专家原生以 MXFP4（4 位浮点，群组大小 32）格式存储，因此权重可以原样加载，无需额外量化和参数卸载即可显著降低显存占用。AMD MI300X 是 AMD 的数据中心 GPU 加速器（OAM 模块形态），以大容量 HBM 高带宽显存著称，通常以包含多张加速卡的整机形式销售。为了让这类大模型在单个 MI300X 上可用，社区改造推理栈以匹配其原生低比特格式，例如 vLLM 处理 FP8 缩放与缓存一致性的补丁，以及 ktransformers 在 CPU 端把 MXFP4 专家重量化为 AMX-INT4 布局。

**「影响」** 对希望在 AMD 硬件上部署 DeepSeek V4 Flash 的开发者或团队，该方案提供了一条经过验证的推理路径，但硬件获取方式（8 卡整机或租赁）和上下文窗口缩减（256K 对 1M）构成了实际部署门槛。

**「社区讨论」** 评论区对硬件可获取性提出质疑，认为 MI300X 不能单卡购买，只能以昂贵的 8 卡整机形式获得。还有人指出先前工作 DwarfStar 也能在更小内存下运行该模型，并认为仅牺牲上下文长度是实用的权衡，但长上下文质量会有所下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ryanzhou/deepseek-v4-flash-mi300x">GitHub - ryanzhou/deepseek-v4-flash-mi300x · GitHub</a></li>
<li><a href="https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/">Bringing up DeepSeek-V4-Flash on AMD MI300X - Fergus Finn</a></li>
<li><a href="https://github.com/kvcache-ai/ktransformers/blob/main/doc/en/DeepSeek-V4-Flash.md">ktransformers/doc/en/DeepSeek-V4-Flash.md at main · kvcache-ai/ktransformers</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#MI300X`, `#LLM Inference`, `#GPU Optimization`, `#Quantization`

---

<a id="item-tech-news-3"></a>
### [Keyv 及关联 npm 包遭 Shai-Hulud 供应链攻击](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

一场名为 Shai-Hulud 的活跃 npm 供应链攻击正在危及 Keyv 及相关包，这些包被广泛用于 Node.js 应用。攻击者可能借安装钩子植入恶意代码，导致依赖链上的项目面临严重风险。该攻击之所以引人关注，是因为 Keyv 生态的高使用量放大了潜在影响，开发者现需审计自身依赖是否受影响。社区同时呼吁对新增的安装前后钩子采取更严格的限制措施，以缓解后续攻击。

hackernews · cimi\_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**「背景」** Keyv 是一个广泛使用的 npm 缓存包，常用于 Node.js 项目。此次攻击中，攻击者先入侵了维护者的 GitHub 账户，随后在 2026 年 8 月 4 日向 keyv 及另外八个相关 npm 包注入了“Mini Shai-Hulud”恶意负载并发布新版本，该蠕虫已传播至超过 400 个不同的 npm 包，CISA 也发布了关于这一 npm 生态系统供应链攻击的警报。

**「影响」** 依赖 Keyv 及相关包的开发者必须立刻检查 lock 文件和 node\_modules 中是否存在恶意安装脚本，并考虑升级或替换受影响的包。由于攻击可能已造成后续连锁攻陷，即便原始仓库被清理，已产生的恶意副本仍可能在网络上持续传播。

**「社区讨论」** 多位用户主张对安装钩子实施新的禁令或暂停批准，认为这是减少此类攻击的关键。还有人建议通过设置 npm 配置项\`min-release-age=5\`来降低风险，并分享了自己整理的 npm 供应链攻击技术文档与生态威胁报告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem">Widespread Supply Chain Compromise Impacting npm Ecosystem | CISA</a></li>
<li><a href="https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack">keyv and cacheable npm Package Hijacked in Supply Chain Attack | Wiz Blog</a></li>
<li><a href="https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack">Keyv and friends compromised in npm supply chain attack</a></li>

</ul>
</details>

**标签**: `#supply-chain-security`, `#npm`, `#open-source`, `#security`, `#devops`

---

<a id="item-tech-news-4"></a>
### [Xbox 宕机导致光盘游戏无法游玩，引发数字所有权争论](https://birchtree.me/blog/xbox-goes-down-you-cant-play-games-you-own-on-disc/) ⭐️ 8.0/10

Xbox 经历了一次大范围宕机，导致玩家连已拥有的光盘版游戏也无法启动，暴露出当前主机对在线验证和 DRM 的依赖。此次事件在 Hacker News 上引发了关于数字版权管理和“真实所有权”的激烈讨论：许多人指出即便购买实体光盘，游戏仍可能因服务器问题而无法使用。社区以 GameCube 等旧主机为例，对比了过去离线可玩的体验，并担忧未来游戏（如 GTA VI）可能无法永久游玩。同时，有观点认为争论焦点不应是实体版与数字版，而应是用户对已购内容应享有离线使用、备份、转售和传承等权利。

hackernews · surprisetalk · 8月4日 12:01 · [社区讨论](https://news.ycombinator.com/item?id=49167448)

**「背景」** Xbox 服务在近期发生的一次大面积中断中，不仅影响了数字版游戏，也导致实体光盘游戏无法启动，尽管微软声称光盘游戏本应可离线游玩。这次事件暴露出 Xbox 的始终在线身份验证机制，使得即使拥有实体光盘，玩家的游戏访问权仍然依赖于微软服务器状态。类似的问题上周也在 PlayStation Network 上出现过，凸显了数字版权管理和服务器依赖对所谓“拥有”游戏的实际影响。

**「影响」** 此次 Xbox 大规模宕机直接导致持有光盘版游戏的玩家在离线或验证失效时无法启动游戏，暴露出数字版权管理（DRM）对“已购买”内容的实际控制力。对玩家而言，这意味着无论购买介质是实体光盘还是数字版，只要服务端不可用，合法拥有的游戏也可能临时变得不可游玩。

**「社区讨论」** 用户 mawadev 分享了在 Steam 上启动《光环：士官长合集》时被迫登录微软账户、经历繁琐验证的遭遇；cautiouscat 将游戏行业与影视、音乐类比对“什么都不再拥有”感到遗憾；paxys 提出无论何种载体都应拥有 6 项权利；unfocso 则赞赏 PS3 时代游戏离线与 LAN 可玩的设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2otOExUWkVSSERDcnBSaGd2RlZpZ0FQAQ?hl=en-US&amp;gl=US&amp;ceid=US:en">Google News - Xbox outage affects physical disc game playback...</a></li>
<li><a href="https://www.remio.ai/post/xbox-disc-lockouts-exposed-a-failure-in-microsofts-offline-licensing-fallback">Xbox Disc Lockouts Exposed a Failure in Microsoft’s Offline Licensing...</a></li>
<li><a href="https://easternherald.com/2026/07/28/xbox-outage-disc-games-microsoft-drm/">Xbox Outage Blocked Disc Games for 12 Hours</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://business.adobe.com/blog/basics/digital-rights-management">Digital Rights Management ( DRM ) | What It Is, How It Works &amp; Why It...</a></li>

</ul>
</details>

**标签**: `#Xbox`, `#DRM`, `#digital ownership`, `#gaming`, `#outage`

---

<a id="item-tech-news-5"></a>
### [为自我改进 AI agent 设计 harness 的工程实践](https://lilianweng.github.io/posts/2026-07-04-harness/) ⭐️ 8.0/10

Lilian Weng 发表了一篇关于为自我改进 AI agent 设计 harness（提示、工具与工作流）的文章，核心思路是把代码库中的 AGENTS.md、技能和工具等“支架”当作可优化对象，并用 trace 驱动自动研究来发现问题。社区实践显示，让 agent 读取大量生产 trace、编写自己的工具（如将加载上下文从 20k tokens/15 次工具调用降至 800 tokens/1 次调用）可显著提升效率；但要实现这类自我改进，必须先建立可靠、准确的 fitness function，并用 eval 和验证/测试集防止 hack。

hackernews · tosh · 8月4日 06:17 · [社区讨论](https://news.ycombinator.com/item?id=49164896)

**「背景」** Lilian Weng 在《Harness Engineering for Self-Improvement》一文中提出“harness engineering”概念，指围绕基础大语言模型构建的系统层，负责规划、工具调用、记忆和评估等机制。她认为，相比单纯改进模型输出，让整个 harness 系统本身成为优化目标、并走向自我改进和自动研究，是更近期的演进方向。这里“harness”指智能体运行所需的提示、技能、工具和评估等外部基础设施，而非字面的“挽具”。

**「影响」** 对使用 agent harness 的开发者，trace 驱动的自动优化已被证实能带来可观效率提升（例如上下文加载由 20k tokens/15 次调用降至 800 tokens/1 次调用），但前提是需要先设计出可靠的 fitness function 和 eval/val-test 划分，否则优化可能奖励取巧行为。

**「社区讨论」** 评论者普遍认为这是 agent 工程的下一个优化方向，但分歧在于如何定义“质量”：有观点认为需要为代码库构建通用 fitness function，也有人怀疑这是“Torment Nexus”式的循环；还有人设想未来 harness 会自己生成 RLHF/DPO 训练集并 LoRA 微调底层模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lilianweng.github.io/posts/2026-07-04-harness/">Harness Engineering for Self - Improvement | Lil&#x27;Log</a></li>
<li><a href="https://www.alphaxiv.org/abs/2607.harness-3">Harness Engineering for Self - Improvement | alphaXiv</a></li>
<li><a href="https://digg.com/tech/gs9h751b">Lilian Weng argues AI self - improvement loops will always require...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#agent engineering`, `#prompt optimization`, `#self-improvement`

---

<a id="item-tech-news-6"></a>
### [MiniMax-H3 的 MLX 移植：在 Apple Silicon 上本地运行视频生成](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 8.0/10

MiniMax 发布了一款名为 MiniMax-H3 的通用全模态生成系统，能够接受文本、图像、音频和视频输入，并可生成最长 15 秒、包含音频的视频片段。PipeNetwork 发布了对应的 MLX 移植包，使其能够在 Apple Silicon 上运行。Simon Willison 在 M5 Max 芯片的 MacBook Pro 上成功运行了该模型，下载了约 115 GB 的模型文件，单次视频生成耗时接近 45 分钟。他得到的视频画面令人印象深刻，但由于没有针对音频提供提示指导，音频输出是“类似语音的垃圾内容”；MiniMax 提供了提示词编写指南来改善这一情况。

rss · Simon Willison · 8月4日 19:10

**「背景」** MiniMax-H3 是一个全模态生成系统，能够统一处理文本、图像、音频和视频，与仅处理单一或少数模态的传统模型不同。MLX 是 Apple 面向 Apple Silicon 的机器学习框架，PipeNetwork 的移植使这类大规模多模态模型可以在 Mac 上本地运行，无需依赖云端服务。

**「影响」** 拥有 Apple Silicon 设备的 AI 从业者现在可以本地运行 MiniMax-H3 来生成带音频的 15 秒视频片段，但需要准备约 115 GB 磁盘空间，并预计每次生成耗时接近 45 分钟；如果不遵循提示词指南设计音频提示，输出音频质量可能很差。

**标签**: `#multimodal AI`, `#MiniMax-H3`, `#MLX`, `#video generation`, `#Apple Silicon`

---

<a id="item-tech-news-7"></a>
### [华为首席科学家警告英伟达式扩展将触及物理极限](https://www.bloomberg.com/news/articles/2026-08-04/huawei-s-top-scientist-warns-of-chip-limit-nvidia-will-soon-face) ⭐️ 8.0/10

华为首席半导体科学家廖恒在 7 月底一场罕见的四小时公开采访中警告，英伟达等芯片巨头通过持续增加计算芯片和高带宽内存来扩展算力的做法终将触及物理极限，一旦跨越就可能出现“雪崩”。他提出华为的替代路径“韬定律”，并透露采用 LogicFolding 技术框架的首款手机芯片将于今年晚些时候亮相。廖恒同时指出，中美半导体产业正分化为两个独立生态系统，各方必须建立完整的制造与供应能力才能生存。这一表态属于专家警告，而非已实现的突破，但反映出行业对现有扩展模式的担忧。

telegram · zaihuapd · 8月4日 08:04

**「背景：韬定律与 LogicFolding」** 华为在 2026 年 5 月于 IEEE 场合提出“韬定律”，将其定义为贯穿器件层、电路层、芯片层和系统层的跨层级优化体系；其中 LogicFolding 通过在电路层“逻辑折叠”缩短关键路径，在芯片层协同软件、架构与芯片，从而在不单纯依赖更先进制程的情况下提升晶体管密度、能效与频率。此前麒麟 2026 被宣传为晶体管密度约 238M Tr/mm²、P 核能效提升 41%、频率达 3.1GHz，但这些数字主要来自厂商及社区传播口径，尚未得到独立验证。廖恒的警告正是在这一背景下，认为单纯堆叠计算芯片和高带宽内存的英伟达式扩展终将触及物理极限。

**「影响」** 这一警告正值中美半导体产业加速“脱钩”：到 2026 年年中，英伟达在华收入已归零，中芯国际推进至 5nm，中国还强制要求国内 AI 算力采用本土芯片。若华为的 LogicFolding 路径兑现，将进一步巩固两个独立生态系统的格局，使依赖单一供应链的全球厂商面临更高分化成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.csdn.net/w776341482/article/details/161422948">调查研究-145 华为韬定律与LogicFolding深度解析：时间缩微如何绕过制程焦虑-CSDN博客</a></li>
<li><a href="https://hwcomputing.csdn.net/6a154001662f9a54cb77215e.html">调查研究-145 华为韬定律与LogicFolding深度解析：时间缩微如何绕过制程焦虑_华为_武子康-鲲鹏升腾开发者社区</a></li>
<li><a href="https://informedclearly.com/en/ai/53995/us-china-chip-war-semiconductor-decoupling-2026">US-China Chip War 2026: Semiconductor Decoupling Deepens</a></li>
<li><a href="https://informedclearly.com/en/geopolitics/58741/global-semiconductor-industry-split-2026">2026: The Year the Global Semiconductor Industry Split in Two</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#Huawei`, `#Nvidia`, `#chip-scaling`, `#tech-decoupling`

---

