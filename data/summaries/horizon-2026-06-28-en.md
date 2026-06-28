# Horizon Daily - 2026-06-28

> From 13 items, 3 important content pieces were selected

---

1. [Using Claude Code for MRI Second Opinion](#item-1) ⭐️ 8.0/10
2. [OpenAI Codex Issue Highlights Sensitive File Exfiltration Risk](#item-2) ⭐️ 8.0/10
3. [KIDS Act Mandates Age Verification for Online Access](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Using Claude Code for MRI Second Opinion](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

A person used Claude Code, an AI coding agent by Anthropic, to analyze their own MRI scan and obtain a second opinion on a shoulder injury diagnosis. This demonstrates a novel, practical application of large language models in healthcare, raising important questions about trust, accuracy, and the role of AI in medical diagnosis. The user uploaded their MRI images to Claude Code and asked it to interpret the findings, comparing the AI's analysis with their doctor's diagnosis. The experiment highlights both the potential and limitations of using general-purpose AI for specialized medical tasks.

hackernews · engmarketer · Jun 28, 16:35 · [Discussion](https://news.ycombinator.com/item?id=48708941)

**Background**: Claude Code is an AI coding agent developed by Anthropic that can read codebases, edit files, and run commands. While primarily designed for software development, users have repurposed it for other tasks like medical image analysis. MRI (Magnetic Resonance Imaging) is a medical imaging technique used to visualize internal structures of the body.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: The discussion includes a radiologist's perspective noting that a full 3D dataset is needed for proper evaluation, and debates about trust in AI versus human experts. Some commenters share personal experiences with misdiagnosis, highlighting the high stakes of medical AI.

**Tags**: `#AI`, `#healthcare`, `#medical imaging`, `#Claude Code`, `#trust`

---

<a id="item-2"></a>
## [OpenAI Codex Issue Highlights Sensitive File Exfiltration Risk](https://github.com/openai/codex/issues/2847) ⭐️ 8.0/10

A GitHub issue (#2847) on the OpenAI Codex repository remains open, discussing the challenge of preventing AI coding agents from exfiltrating sensitive files. Community members argue that system-level controls like file permissions and containers are more effective than feature-level blocklists. This discussion is critical because AI coding agents like Codex can inadvertently access and upload sensitive data, posing security risks for developers and enterprises. The outcome may influence how future AI agents handle file access and privacy. The issue proposes an opt-out approach for sensitive files, but commenters note that LLMs can leak data through tool outputs (e.g., grep results). Some advocate for opt-in file access and sandboxing, while others warn that a blocklist alone provides a false sense of security.

hackernews · pikseladam · Jun 28, 12:27 · [Discussion](https://news.ycombinator.com/item?id=48706714)

**Background**: OpenAI Codex is an AI coding agent that can autonomously perform software engineering tasks, such as writing and editing code. It operates by executing commands and accessing files on the user's system, which raises concerns about accidental exposure of sensitive information like API keys or credentials.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (168 points, 115 comments) shows strong consensus that system-level solutions (chmod, containers) are superior to feature-level blocklists. Users share real-world implementations, such as NVIDIA's open-sourced Rumpelpod for secure devcontainers, and emphasize that opt-in access is essential.

**Tags**: `#security`, `#AI coding agents`, `#OpenAI Codex`, `#file permissions`, `#sandboxing`

---

<a id="item-3"></a>
## [KIDS Act Mandates Age Verification for Online Access](https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online) ⭐️ 8.0/10

The KIDS Act, introduced in the U.S. Congress, would require websites to verify users' ages before granting access, as analyzed by the Electronic Frontier Foundation (EFF). This legislation could fundamentally alter internet access by mandating age checks, raising serious privacy and free speech concerns that affect all users, not just children. The bill is sponsored by Brett Guthrie (R-KY) and co-sponsored by Frank Pallone (D-NJ), with major donors including Alphabet and AIPAC according to OpenSecrets.

hackernews · bilsbie · Jun 28, 11:56 · [Discussion](https://news.ycombinator.com/item?id=48706560)

**Background**: Age verification technologies, such as those offered by AgeGO and Yoti, aim to check user ages while protecting privacy. The EFF is a digital rights group that advocates for civil liberties online and opposes mandatory age verification as a threat to anonymity and free expression.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation">Electronic Frontier Foundation</a></li>
<li><a href="https://www.agego.com/">Instant & Safe Online Age Verification | AgeGO | AgeGO - Online Age ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the research linking social media to mental health, noted the irony of requiring personal information after years of advice to keep it private, and speculated about international lobbying efforts behind such laws.

**Tags**: `#age verification`, `#internet regulation`, `#privacy`, `#EFF`, `#policy`

---

