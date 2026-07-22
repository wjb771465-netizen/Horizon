# Horizon 每日速递 - 2026-07-22

> From 16 items, 4 important content pieces were selected

---

1. [陶哲轩用 ChatGPT 探索雅可比猜想](#item-1) ⭐️ 8.0/10
2. [Bento：一个离线可用的完整幻灯片编辑器，仅一个 HTML 文件](#item-2) ⭐️ 8.0/10
3. [初创公司 Postgres 生存指南](#item-3) ⭐️ 8.0/10
4. [面试项目隐藏恶意 Git 钩子](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [陶哲轩用 ChatGPT 探索雅可比猜想](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) ⭐️ 8.0/10

陶哲轩分享了一段 ChatGPT 对话，他利用 AI 探索雅可比猜想的一个反例，展示了先进的 AI 辅助数学推理。对话中，陶哲轩提出精确问题，引导模型理解复杂的代数几何概念。 这标志着大型语言模型如何协助顶尖数学家进行研究的重要示范，可能加速发现和合作。它也凸显了 AI 在数学形式推理和问题解决中不断演变的角色。 该反例由 Levent Alpöge 于 2026 年 7 月使用 Claude Fable 5 发现，否定了维度大于 2 时的雅可比猜想。陶哲轩的对话显示他使用 ChatGPT 来验证和理解该多项式反例的结构。

hackernews · gmays · Jul 22, 17:30 · [社区讨论](https://news.ycombinator.com/item?id=49010345)

**背景**: 雅可比猜想是代数几何中的一个长期难题，它断言如果多项式映射的雅可比行列式是非零常数，则该映射必有多项式逆。该猜想最初于 1884 年针对两个变量提出，后来推广到一般情况，但尽管有许多尝试证明，仍悬而未决超过一个世纪。陶哲轩是菲尔兹奖得主，以其在多个数学领域的贡献而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao</a></li>

</ul>
</details>

**社区讨论**: 评论者对陶哲轩对 ChatGPT 的专业使用感到着迷，指出他精确的提问和深厚的领域知识使他能够提取有价值的见解。一些人强调该反例并非暴力搜索得到，而是具有结构上的重要性，并且陶哲轩的交互模式反映了专家如何有效利用 LLM。

**标签**: `#mathematics`, `#AI`, `#ChatGPT`, `#research`, `#LLM`

---

<a id="item-2"></a>
## [Bento：一个离线可用的完整幻灯片编辑器，仅一个 HTML 文件](https://bento.page/slides/) ⭐️ 8.0/10

Bento 是一个约 560KB 的单一 HTML 文件，包含了完整的幻灯片编辑器，支持动画、实时协作和离线使用，无需安装或云登录。 这展示了一种本地优先、可移植应用的新范式，无需依赖云服务即可轻松共享和编辑，有望减少对大型演示工具的依赖。 该文件使用 JSON 块存储幻灯片数据，并通过 base64 编码的应用 blob 在浏览器中用 DecompressionStream 解压，保持包体积小巧。协作通过加密盲中继实现，中继无法看到数据内容。

hackernews · starfallg · Jul 22, 15:19 · [社区讨论](https://news.ycombinator.com/item?id=49008211)

**背景**: 传统的幻灯片编辑器如 PowerPoint 或 Google Slides 需要安装或云连接。单文件 Web 应用将所有资源打包到一个 HTML 文件中，支持离线使用和轻松分发。本地优先架构优先考虑客户端数据和离线能力，减少对服务器的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Single-File_HTML_Utilities">Single-File HTML Utilities</a></li>
<li><a href="https://techbuzzonline.com/local-first-software-architecture-guide/">Local-First Software Architecture: Beginner’s Guide to ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区称赞了 Bento 的创新，创建者解释了其架构。一些用户指出在大量并发编辑时存在性能问题，其他人则讨论了本地优先软件和单文件应用的更广泛趋势。

**标签**: `#presentation-tools`, `#single-file-app`, `#offline-first`, `#web-development`, `#local-first`

---

<a id="item-3"></a>
## [初创公司 Postgres 生存指南](https://hatchet.run/blog/postgres-survival-guide) ⭐️ 8.0/10

一份面向使用 PostgreSQL 的初创公司的实用指南已发布，涵盖了扩展和维护数据库时的常见陷阱与最佳实践。 该指南针对许多初创公司在成长过程中面临的关键问题，帮助它们避免代价高昂的错误并提高数据库可靠性。 该指南包括使用 UUIDv7 而非 UUIDv4、确定性排序锁以避免死锁，以及使用 EXPLAIN (GENERIC_PLAN)进行查询分析等建议。

hackernews · abelanger · Jul 22, 12:36 · [社区讨论](https://news.ycombinator.com/item?id=49005787)

**背景**: PostgreSQL 是一种流行的开源关系型数据库，被许多初创公司使用。随着数据增长，慢查询、死锁和备份失败等常见问题可能威胁运营。该指南旨在提供可操作的解决方案。

**社区讨论**: 评论者指出了备份策略等缺失主题，并推荐了 Barman 等工具。他们还讨论了 ORM 的使用、级联删除和仅追加模式，提供了额外的见解和修正。

**标签**: `#PostgreSQL`, `#startups`, `#database`, `#best practices`, `#scaling`

---

<a id="item-4"></a>
## [面试项目隐藏恶意 Git 钩子](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/) ⭐️ 8.0/10

一名安全研究人员发现，一份居家编程测试中包含一个恶意 Git 钩子，该钩子会静默执行远程负载，标志着招聘过程中出现了一种新型攻击手段。 这一事件凸显了通过看似合法的面试任务针对开发者的供应链攻击趋势日益增长，对求职者和公司都构成风险。 该恶意钩子会检查受害者的操作系统，并使用原始 IP 地址获取负载，可能导致开发者机器上的远程代码执行。

hackernews · CITIZENDOT · Jul 22, 20:33 · [社区讨论](https://news.ycombinator.com/item?id=49013036)

**背景**: Git 钩子是在 Git 工作流程的某些节点（如提交前）自动运行的脚本。攻击者可以在仓库中嵌入恶意钩子，当开发者执行常见的 Git 操作时执行任意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sscsecurity.dev/book1/chapter-08/ch-8.5/">Git -Specific Attack Vectors - Open Source Software Supply Chain...</a></li>
<li><a href="https://github.com/muasif80/git-hook-guard">GitHub - muasif80/ git - hook -guard: Auto-scans opened Git repositories...</a></li>
<li><a href="https://www.invicti.com/learn/remote-code-execution-rce">Remote Code Execution (RCE)</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，这种攻击手段正成为反复出现的主题，上个月 Hacker News 上就有类似故事。一些人批评使用原始 IP 地址是明显的恶意软件标志，而另一些人则争论 Claude 的安全防护是否妨碍了其作为助手的实用性。

**标签**: `#malware`, `#security`, `#git`, `#interview`, `#supply chain attack`

---

