# Horizon 每日速递 - 2026-06-28

> From 13 items, 3 important content pieces were selected

---

1. [用 Claude Code 获取 MRI 第二意见](#item-1) ⭐️ 8.0/10
2. [OpenAI Codex 问题凸显敏感文件泄露风险](#item-2) ⭐️ 8.0/10
3. [《KIDS 法案》要求在线年龄验证](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [用 Claude Code 获取 MRI 第二意见](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

有人使用 Anthropic 的 AI 编程代理 Claude Code 分析自己的 MRI 扫描，为肩部损伤诊断获取第二意见。 这展示了大语言模型在医疗领域的新颖实用应用，引发了对信任、准确性以及 AI 在医疗诊断中角色的重要讨论。 用户将 MRI 图像上传到 Claude Code，要求其解读结果，并将 AI 的分析与医生的诊断进行比较。该实验突显了使用通用 AI 处理专业医疗任务的潜力和局限性。

hackernews · engmarketer · Jun 28, 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude Code 是 Anthropic 开发的 AI 编程代理，可以读取代码库、编辑文件和运行命令。虽然主要用于软件开发，但用户将其重新用于医学图像分析等任务。MRI（磁共振成像）是一种用于可视化身体内部结构的医学成像技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 讨论包括一位放射科医生的观点，指出需要完整的 3D 数据集才能进行正确评估，以及关于信任 AI 还是人类专家的辩论。一些评论者分享了误诊的个人经历，突显了医疗 AI 的高风险性。

**标签**: `#AI`, `#healthcare`, `#medical imaging`, `#Claude Code`, `#trust`

---

<a id="item-2"></a>
## [OpenAI Codex 问题凸显敏感文件泄露风险](https://github.com/openai/codex/issues/2847) ⭐️ 8.0/10

OpenAI Codex 仓库中的一个 GitHub issue（#2847）仍未关闭，讨论如何防止 AI 编码代理泄露敏感文件。社区成员认为，文件权限和容器等系统级控制比功能级黑名单更有效。 这一讨论至关重要，因为像 Codex 这样的 AI 编码代理可能无意中访问并上传敏感数据，给开发者和企业带来安全风险。其结果可能影响未来 AI 代理处理文件访问和隐私的方式。 该 issue 提出对敏感文件采用 opt-out 方式，但评论者指出 LLM 可能通过工具输出（如 grep 结果）泄露数据。一些人主张 opt-in 文件访问和沙箱化，而另一些人警告仅靠黑名单会带来虚假的安全感。

hackernews · pikseladam · Jun 28, 12:27 · [社区讨论](https://news.ycombinator.com/item?id=48706714)

**背景**: OpenAI Codex 是一种 AI 编码代理，可以自主执行软件工程任务，如编写和编辑代码。它通过执行命令和访问用户系统上的文件来运行，这引发了关于意外暴露 API 密钥或凭据等敏感信息的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（168 分，115 条评论）显示出强烈共识：系统级解决方案（chmod、容器）优于功能级黑名单。用户分享了实际实现，如 NVIDIA 开源的 Rumpelpod 用于安全开发容器，并强调 opt-in 访问是必要的。

**标签**: `#security`, `#AI coding agents`, `#OpenAI Codex`, `#file permissions`, `#sandboxing`

---

<a id="item-3"></a>
## [《KIDS 法案》要求在线年龄验证](https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online) ⭐️ 8.0/10

该法案通过强制年龄验证可能从根本上改变互联网访问方式，引发严重的隐私和言论自由问题，影响所有用户，而不仅仅是儿童。 该法案由 Brett Guthrie（共和党-肯塔基州）提出，Frank Pallone（民主党-新泽西州）共同发起，根据 OpenSecrets 数据，主要捐赠者包括 Alphabet 和 AIPAC。

hackernews · bilsbie · Jun 28, 11:56 · [社区讨论](https://news.ycombinator.com/item?id=48706560)

**背景**: 年龄验证技术（如 AgeGO 和 Yoti 提供的服务）旨在检查用户年龄的同时保护隐私。EFF 是一个倡导网络公民自由的数字权利组织，反对强制年龄验证，认为其威胁匿名性和言论自由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation">Electronic Frontier Foundation</a></li>
<li><a href="https://www.agego.com/">Instant & Safe Online Age Verification | AgeGO | AgeGO - Online Age ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对社交媒体与心理健康关联的研究表示怀疑，指出多年来建议保护个人信息如今却要求提供个人信息的讽刺，并猜测此类法律背后存在国际游说努力。

**标签**: `#age verification`, `#internet regulation`, `#privacy`, `#EFF`, `#policy`

---

