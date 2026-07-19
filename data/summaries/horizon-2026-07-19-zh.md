# Horizon 每日速递 - 2026-07-19

> From 10 items, 4 important content pieces were selected

---

1. [阿里巴巴发布 Qwen 3.8，2.4 万亿参数开源大模型](#item-1) ⭐️ 9.0/10
2. [用 1600 美元的 ESP32 替代 12 万美元的保龄球计分系统](#item-2) ⭐️ 8.0/10
3. [Claude Code 采用 Rust 重写的 Bun](#item-3) ⭐️ 8.0/10
4. [Moonshot AI 因需求暂停 Kimi K3 新订阅](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [阿里巴巴发布 Qwen 3.8，2.4 万亿参数开源大模型](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) ⭐️ 9.0/10

阿里巴巴宣布推出 Qwen 3.8，这是一个 2.4 万亿参数的开源大语言模型，以回应 Moonshot AI 的 Kimi K3。该模型预计很快将在 Hugging Face 上发布。 这标志着开源大模型竞赛的重大升级，阿里巴巴与 Moonshot AI 竞相发布最大的开源模型。这种竞争使 AI 社区受益，提供了更强大、可本地部署的模型。 Qwen 3.8 拥有 2.4 万亿参数，略小于 Kimi K3 的 2.8 万亿。阿里巴巴已确认该模型将开源权重，社区成员正热切期待其发布以进行本地部署。

hackernews · nh43215rgb · Jul 19, 08:44 · [社区讨论](https://news.ycombinator.com/item?id=48966120)

**背景**: 拥有万亿参数的大语言模型通常太大而无法在消费级硬件上运行，但开源权重允许研究人员和开发者在强大服务器上进行微调和部署。阿里巴巴的 Qwen 系列和 Moonshot AI 的 Kimi 系列是领先的中国大模型家族，在全球范围内竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48966120">Qwen 3 . 8 is launching and going open-weight soon | Hacker News</a></li>
<li><a href="https://huggingface.co/Qwen">Org profile for Qwen on Hugging Face, the AI community building the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户对竞争和本地部署可能性感到兴奋。一些用户对 Qwen 之前的模型表示不满，而另一些用户则称赞较小 Qwen 变体在本地使用中的表现。

**标签**: `#AI`, `#LLM`, `#open-source`, `#Alibaba`, `#machine learning`

---

<a id="item-2"></a>
## [用 1600 美元的 ESP32 替代 12 万美元的保龄球计分系统](https://news.ycombinator.com/item?id=48968606) ⭐️ 8.0/10

一位站点可靠性工程师用 ESP32 微控制器构建的自定义方案，以仅 1600 美元的成本替代了价值 12 万美元的专有保龄球计分系统。 该项目展示了现代低成本嵌入式系统如何颠覆昂贵的供应商锁定工业设备，可能为小企业节省数千美元，并赋予他们对硬件和数据的完全控制权。 该系统采用 ESP-NOW 星型拓扑网状网络，并配有 RS485 有线回退，数据上报到运行 Redis 和状态机的树莓派，前端基于 React。作者计划将整个技术栈作为 OpenLaneLink 开源。

hackernews · section33 · Jul 19, 14:41

**背景**: 保龄球计分系统集成了球瓶检测、球速、犯规检测和动画等功能，通常作为专有软件包出售，8 条球道的成本在 8 万到 12 万美元之间。ESP32 是一种低成本微控制器，内置 Wi-Fi 和蓝牙，广泛用于物联网和嵌入式项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>
<li><a href="https://www.digikey.com/en/maker/blogs/2024/a-guide-for-the-esp32-microcontroller-series">A Guide for the ESP32 Microcontroller Series</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞该项目验证了用现代嵌入式技术改造旧系统的可行性。一位用户分享了类似的使用机械迷你保龄球道的经历，另一位则对添加 LED 灯带追逐效果和自助支付终端集成表示兴趣。

**标签**: `#ESP32`, `#embedded systems`, `#retrofitting`, `#DIY`, `#SRE`

---

<a id="item-3"></a>
## [Claude Code 采用 Rust 重写的 Bun](https://simonwillison.net/2026/Jul/19/claude-code-in-bun-in-rust/#atom-everything) ⭐️ 8.0/10

Simon Willison 确认 Claude Code v2.1.181 及更高版本使用了 Rust 移植的 Bun，在 Linux 上启动速度提升了 10%。证据包括嵌入的 Rust 源文件路径以及比最新公开版本更新的 Bun 版本号（v1.4.0）。 这表明一款重要的 AI 编程工具正在使用 Rust 重写的运行时投入生产，凸显了 Rust 在性能关键型基础设施中日益增长的作用。这也显示了 Anthropic 与其收购的 Bun 的深度整合，以及重写在可靠性和速度方面的实际好处。 Bun 的 Rust 移植尚未作为稳定版本公开发布；Claude Code 搭载的是仅作为 canary 版本提供的预览版（v1.4.0）。重写作为一个巨大的 PR 在不到一个月内合并，团队指出 Rust 的自动内存管理是相比 Zig 减少错误的关键原因。

rss · Simon Willison · Jul 19, 03:54 · [社区讨论](https://news.ycombinator.com/item?id=48966569)

**背景**: Bun 是一个 JavaScript 运行时，旨在作为 Node.js 的直接替代品，最初用 Zig 编写。Claude Code 是 Anthropic 的终端代理编程工具。Bun 的 Rust 重写由 Bun 的创建者 Jarred Sumner 宣布，Anthropic 在今年早些时候收购了 Bun。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://code.claude.com/docs/en/how-claude-code-works">How Claude Code works - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人质疑为什么一个 TUI 需要 JavaScript 运行时，而另一些人则欣赏用 Rust 替代 Zig 的技术理由。有人对项目的治理和重写的速度表示担忧，认为关于变更的沟通不够充分。

**标签**: `#Claude Code`, `#Bun`, `#Rust`, `#JavaScript runtime`, `#Anthropic`

---

<a id="item-4"></a>
## [Moonshot AI 因需求暂停 Kimi K3 新订阅](https://twitter.com/kimi_moonshot/status/2078855608565207130) ⭐️ 8.0/10

Moonshot AI 宣布，由于其旗舰模型 Kimi K3 需求过大，暂时停止新订阅，优先保障现有用户的算力资源。 此举表明 Kimi K3（一个拥有 2.8 万亿参数、可与美国顶级系统匹敌的开源模型）极受欢迎，也凸显了在竞争激烈的 AI 领域中以客户为先的策略。 Kimi K3 采用名为 Kimi Delta Attention (KDA)的混合线性注意力机制，其 RNN/线性注意力层数量是全注意力层的 3 倍，并支持 100 万 token 的上下文窗口。

hackernews · serialx · Jul 19, 16:02 · [社区讨论](https://news.ycombinator.com/item?id=48969291)

**背景**: Moonshot AI 是一家中国公司，开发了 Kimi 聊天机器人和大型语言模型。Kimi K3 于 2025 年 7 月发布，是其最强大的模型，拥有 2.8 万亿参数，成为有史以来最大的开源模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems">China’s Moonshot AI releases Kimi K3, the largest open-source model ever, rivaling top U.S. systems | VentureBeat</a></li>

</ul>
</details>

**社区讨论**: 社区评论称赞 Moonshot AI 优先考虑现有用户而非快速增长，一位用户分享了快速用尽每日配额的亲身经历。另一条评论则强调了拥有大量 RNN/线性注意力层的技术创新。

**标签**: `#AI`, `#Moonshot AI`, `#Kimi K3`, `#subscription`, `#demand`

---

