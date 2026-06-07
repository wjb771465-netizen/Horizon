# Horizon 每日速递 - 2026-06-07

> From 49 items, 4 important content pieces were selected

---

1. [LLM 正在侵蚀软件工程职业](#item-1) ⭐️ 8.0/10
2. [Lathe：用 LLM 生成动手教程，帮助学习而非替代学习](#item-2) ⭐️ 8.0/10
3. [第 29 届 IOCCC 获奖者揭晓，令人瞠目的混淆 C 代码](#item-3) ⭐️ 8.0/10
4. [Jane Street 工程师改用 Claude 做 UI 设计](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [LLM 正在侵蚀软件工程职业](https://human-in-the-loop.bearblog.dev/llms-are-eroding-my-software-engineering-career-and-i-dont-know-what-to-do/) ⭐️ 8.0/10

一位软件工程师发表个人叙述，表达了对大型语言模型（LLM）正在侵蚀其职业生涯的深切担忧，在 Hacker News 上引发了丰富的社区讨论，获得 745 分和 717 条评论。 这场辩论凸显了软件工程师对 AI 影响其职业日益增长的焦虑，社区细致入微的回应既揭示了 LLM 当前的局限性，也表达了对未来快速改进的担忧。 作者认为 LLM 正在侵蚀其职业生涯的三大支柱：深层系统知识、业务领域专业知识以及对 AI 输出进行批判的能力。评论者反驳说，LLM 在复杂业务逻辑和特定领域任务上仍然失败，但承认进展迅速。

hackernews · poisonfountain · Jun 7, 12:49 · [社区讨论](https://news.ycombinator.com/item?id=48434312)

**背景**: 大型语言模型（LLM）如 GPT-4 是经过大量文本数据训练的人工智能系统，能够生成类似人类的文本。它们越来越多地被用于软件开发中的代码生成、调试和重构，引发了关于人类程序员未来角色的疑问。

**社区讨论**: 评论者意见分歧：一些人认为 LLM 在复杂任务（如金融产品、地方税务法规）上仍缺乏可靠性，而另一些人则警告说快速改进可能很快克服当前障碍。少数人强调，人类的关怀和坚持解决问题的意愿仍然不可替代。

**标签**: `#LLMs`, `#software engineering`, `#career impact`, `#AI debate`, `#community discussion`

---

<a id="item-2"></a>
## [Lathe：用 LLM 生成动手教程，帮助学习而非替代学习](https://github.com/devenjarvis/lathe) ⭐️ 8.0/10

Lathe 是一个 Go 语言编写的命令行工具，它利用 LLM（如 Claude Code、Cursor、Codex）为任何技术主题生成交互式、有来源支持的教程，用户通过在本地的 Web 界面中手动输入代码来学习。 该工具解决了人们对 LLM 绕过学习过程的担忧，它鼓励主动动手参与而非被动代码生成，可能改变开发者利用 AI 学习新领域的方式。 Lathe 生成的教程包含目录、旁注、练习和来源引用；它还支持验证教程能否编译运行，以及扩展更多章节。该工具是一个低风险的个人项目，目前主要在 macOS 上的 Claude Code 环境中测试。

hackernews · devenjarvis · Jun 7, 11:16 · [社区讨论](https://news.ycombinator.com/item?id=48433756)

**背景**: 大型语言模型（LLM）如 GPT-4 和 Claude 越来越多地被用于编码助手，能够根据自然语言提示生成代码。然而，许多教育者和学习者担心依赖这些工具生成完整代码会阻碍深入理解和技能发展。Lathe 颠覆了这一范式，它利用 LLM 创建结构化的分步教程，要求学习者主动输入代码并参与其中，类似于传统的动手学习方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ideaverse.ai/blog/lathe-using-llms-to-teach-new-domains-via-hands-on-tutorials-mq43c7mo">Lathe: using LLMs to teach new domains via hands-on tutorials</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(code_editor)">Cursor (code editor)</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这一概念，并分享了相关方法，例如苏格拉底式问答——让 LLM 提出逐步深入的问题以迫使主动思考。多位用户提到他们构建了类似的技能或命令行工具来生成教程和执行摘要，这表明人们对将 LLM 用于主动学习而非被动消费有浓厚兴趣。

**标签**: `#LLM`, `#education`, `#learning`, `#tutorial`, `#CLI`

---

<a id="item-3"></a>
## [第 29 届 IOCCC 获奖者揭晓，令人瞠目的混淆 C 代码](https://www.ioccc.org/2025/) ⭐️ 8.0/10

第 29 届国际混淆 C 代码竞赛（IOCCC）于 2025 年 8 月公布获奖者，共有 23 个获奖作品，其中包括一个源代码视觉上像 GameBoy 游戏机的 GameBoy 模拟器，以及一个仅 366 字节却能运行 Linux 和 Doom 的模拟器。 这些作品展示了 C 语言编程中极致的创造力和技术技巧，突破了用最少代码所能实现的极限。该竞赛持续激励着全球程序员，并凸显了 C 语言作为底层创新语言的持久魅力。 GameBoy 模拟器由 rclone 的作者 Nick Craig-Wood 创建，其代码形状像 GameBoy 游戏机。366 字节的模拟器实现了单指令集计算机（OISC）架构，展示了令人惊叹的功能压缩。

hackernews · matt_d · Jun 7, 05:47 · [社区讨论](https://news.ycombinator.com/item?id=48432199)

**背景**: IOCCC 是一项编程竞赛，挑战参与者编写尽可能具有创意混淆的 C 代码，以庆祝 C 语言的语法晦涩。参赛作品匿名评审，获奖者在官方网站上获得表彰。该竞赛自 1984 年开始举办，期间有间断，2025 年是第 29 届。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IOCCC">IOCCC</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_Obfuscated_C_Code_Contest">International Obfuscated C Code Contest - Wikipedia</a></li>
<li><a href="https://medium.com/@3641/international-obfuscated-c-code-contest-ioccc-eda55a9381f1">International Obfuscated C Code Contest ( IOCCC ). Let’s talk... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 GameBoy 模拟器的视觉代码设计和 366 字节模拟器运行 Linux 和 Doom 的能力表示惊叹。有人指出 IOCCC 明确允许在指南中使用 LLM，也有人希望 Underhanded C Contest 能够回归。

**标签**: `#IOCCC`, `#obfuscated C`, `#programming contest`, `#emulator`, `#creative coding`

---

<a id="item-4"></a>
## [Jane Street 工程师改用 Claude 做 UI 设计](https://blog.janestreet.com/i-design-with-claude-code-more-than-figma-now-index/) ⭐️ 8.0/10

一位 Jane Street 工程师描述了自己从 Figma 转向使用 Claude 进行 UI 原型设计的过程，直接生成功能代码而非静态模型。 这一转变凸显了 AI 在设计领域日益重要的作用，实现了快速迭代并模糊了设计与实现之间的界限，可能改变设计师与开发者的协作方式。 该工程师在 Jane Street 的期权交易台工作，使用 OCaml 和 Bonsai 框架，Claude 生成直接实现设计的代码，绕过了传统的规格文档和 Figma 模型。

hackernews · MrBuddyCasino · Jun 7, 05:04 · [社区讨论](https://news.ycombinator.com/item?id=48431981)

**背景**: Claude 是 Anthropic 的 AI 助手，Claude Design 是 Anthropic Labs 推出的用于创建视觉作品的新产品。Figma 是流行的 UI 设计工具。Jane Street 是一家以使用 OCaml 闻名的量化交易公司。该工程师的方法代表了 AI 从设计意图生成生产就绪代码的新范式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.janestreet.com/i-design-with-claude-code-more-than-figma-now-index/">Jane Street Blog - I design with Claude more than Figma now</a></li>
<li><a href="https://www.anthropic.com/news/claude-design-anthropic-labs">Introducing Claude Design by Anthropic Labs \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论包括对业务方使用 AI 绕过设计过程的怀疑，指出 Jane Street 是 Anthropic 的投资方，对迭代成本的疑问，以及关于设计师是否应该编码的辩论。有人指出设计看起来相似且遵循当代网页套路。

**标签**: `#AI-assisted design`, `#Claude`, `#UI/UX`, `#design tools`, `#Jane Street`

---

