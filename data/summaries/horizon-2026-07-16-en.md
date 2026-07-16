# Horizon Daily - 2026-07-16

> From 40 items, 8 important content pieces were selected

---

1. [Thinking Machines Lab Releases Inkling Open-Weight Model](#item-1) ⭐️ 9.0/10
2. [Linus Torvalds Endorses AI in Linux Kernel Development](#item-2) ⭐️ 9.0/10
3. [xAI Open-Sources Grok Build After Privacy Backlash](#item-3) ⭐️ 9.0/10
4. [Moonshot AI Releases Frontier-Level Open-Weight Model Kimi K3](#item-4) ⭐️ 8.0/10
5. [Roc Compiler Rewrite from Rust to Zig Progress](#item-5) ⭐️ 8.0/10
6. [GPT-5.6 Codex Bug Deletes User Files](#item-6) ⭐️ 8.0/10
7. [NVIDIA Nemotron-3 Embed Tops RTEB Benchmark](#item-7) ⭐️ 8.0/10
8. [Hugging Face Discloses July 2026 Security Incident](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Thinking Machines Lab Releases Inkling Open-Weight Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Mira Murati's Thinking Machines Lab released Inkling, a 975B total parameter (41B active) Mixture-of-Experts multimodal model under Apache-2.0 license, trained on 45 trillion tokens of text, images, audio, and video. This release marks a significant entry into the open-weight AI ecosystem from a high-profile lab, providing a competitive alternative to Chinese open-weight models and strengthening the US open-weight landscape alongside NVIDIA Nemotron and Gemma 4. Inkling is not a frontier model but a strong base for fine-tuning via the Tinker platform; its model card and training data documentation are notably sparse, lacking detailed information about data sources and composition.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is a transformer architecture that uses multiple specialized sub-networks (experts) and a gating mechanism to activate only a subset of experts per input, enabling large total parameter counts with lower computational cost. Open-weight models allow users to download, run, and modify the model weights, promoting transparency and customization. Apache-2.0 is a permissive license that permits free use, modification, and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained - Hugging Face</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Thinking Machines Lab`

---

<a id="item-2"></a>
## [Linus Torvalds Endorses AI in Linux Kernel Development](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 9.0/10

Linus Torvalds, the creator of Linux, stated on the Linux Media mailing list that Linux is not an anti-AI project and that AI is a clearly useful tool, challenging those who disagree to fork or leave. This definitive endorsement from the top-level maintainer signals a major paradigm shift in the open-source community, potentially accelerating AI integration in kernel development and influencing other projects. Torvalds emphasized that AI's usefulness is no longer in question, though he acknowledged other open questions about AI's economy. The statement was made on the Linux Media mailing list, a key venue for kernel development discussions.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and long-time maintainer of the Linux kernel, the core of the Linux operating system. The kernel development community has historically had diverse opinions on incorporating AI tools, with some opposing their use due to concerns about code quality, licensing, or ethical issues. Torvalds' statement effectively settles the debate within the Linux project, at least for now.

**Tags**: `#Linux`, `#AI`, `#Open Source`, `#Linus Torvalds`, `#Kernel Development`

---

<a id="item-3"></a>
## [xAI Open-Sources Grok Build After Privacy Backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI has open-sourced the entire Grok Build codebase under the Apache 2.0 license after users discovered that the CLI tool uploaded entire directories to cloud storage, including sensitive files like SSH keys and password databases. This incident highlights critical privacy risks in AI-powered developer tools and demonstrates how community backlash can force rapid corporate action, including open-sourcing proprietary code to rebuild trust. The codebase contains 844,530 lines of Rust (only ~3% vendored) and includes a self-contained terminal renderer for Mermaid diagrams. xAI has deleted all previously retained user data and disabled default data retention.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is an AI-powered coding assistant from xAI that runs as a CLI tool. It uses large language models to help developers write code, but was found to upload entire project directories to Google Cloud without explicit user consent, sparking severe privacy concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/15/grok-build/">xai-org/grok-build, now open source</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/965600/spacexai-grok-build-repository-upload">SpaceXAI’s Grok programming tool was uploading its users’ entire codebase to cloud storage | The Verge</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#open-source`, `#AI`, `#security`, `#xAI`

---

<a id="item-4"></a>
## [Moonshot AI Releases Frontier-Level Open-Weight Model Kimi K3](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI has released Kimi K3, a frontier-level open-weight large language model that claims performance second only to Claude Fable 5 and GPT-5.6 Sol, with full model weights to be released in the coming days. This release marks a significant step in commoditizing frontier AI capabilities, as a Chinese lab provides open access to a model competitive with top proprietary systems, potentially accelerating innovation and lowering barriers for developers worldwide. Kimi K3 is available via OpenRouter API with pricing at $3 per million input tokens and $15 per million output tokens, and it supports reasoning tokens. The model's full weights, architecture details, and technical report are promised soon.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: An open-weight model is an AI model whose trained parameters (weights) are publicly released, allowing anyone to download, run, study, and modify it. This contrasts with closed models like GPT-4, where only API access is provided. Frontier-level models represent the highest tier of AI performance, typically achieved by large-scale training.

<details><summary>References</summary>
<ul>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about Moonshot's data usage policy, which allows training on API content unless enterprise arrangements are made. Some see this as a move toward commoditizing AI intelligence, while others note the high cost and effort still required for such models.

**Tags**: `#AI`, `#open-source`, `#large language models`, `#China`, `#machine learning`

---

<a id="item-5"></a>
## [Roc Compiler Rewrite from Rust to Zig Progress](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

The Roc team has achieved feature parity with the original Rust compiler after rewriting 300,000 lines of Rust code into Zig over the past year and a half. This rewrite highlights the trade-offs between Rust's safety guarantees and Zig's simplicity and incremental build speed, which could influence future systems programming language choices for performance-critical projects. The blog post emphasizes that compilers emitting machine code often need memory-unsafe operations, and Zig's ReleaseSafe mode catches use-after-free errors via runtime checks, though some community members question the extent of these checks.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Roc is a functional programming language focused on speed and friendliness. Its compiler was originally written in Rust, but the team decided to rewrite it in Zig to leverage Zig's faster incremental builds and simpler memory model, despite Rust's stronger safety guarantees.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/roc-lang/roc">GitHub - roc-lang/roc: A fast, friendly, functional language. The Roc Programming Language roc/docs/mini-tutorial-new-compiler.md at main · roc-lang/roc ROCm Software - AMD The Complete Roc Guide: From Zero to Expert - kodikra How Our Rust-to-Zig Rewrite is Going</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://ziglang.org/">Home ⚡ Zig Programming Language</a></li>

</ul>
</details>

**Discussion**: Notable figures like steveklabnik argued that memory-unsafe operations are not as pervasive in compilers as the post suggests, while landr0id questioned Zig's ability to catch use-after-free errors. Others praised Zig's incremental builds as a killer feature but expressed concern about losing Rust's safety.

**Tags**: `#Rust`, `#Zig`, `#compiler`, `#systems programming`, `#performance`

---

<a id="item-6"></a>
## [GPT-5.6 Codex Bug Deletes User Files](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

A bug in GPT-5.6's Codex can accidentally delete user files when full access mode is enabled without sandboxing, and the model mistakenly deletes $HOME instead of a temporary directory. This bug highlights critical safety risks in AI coding agents that have unrestricted file system access, potentially causing irreversible data loss for developers and enterprises relying on such tools. The bug occurs when full access mode is enabled, sandboxing protections are disabled, and auto review is turned off; the model attempts to override $HOME to define a temporary directory but mistakenly deletes $HOME instead.

rss · Simon Willison · Jul 16, 17:45

**Background**: GPT-5.6 Codex is an AI coding agent that can execute commands on the user's system. Full access mode grants it broad permissions, while sandboxing isolates its actions to prevent harm. The $HOME environment variable points to the user's home directory, which contains personal files and settings.

<details><summary>References</summary>
<ul>
<li><a href="https://www.docker.com/products/docker-sandboxes/">Sandboxes for Coding Agents - Docker</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor ...</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-7"></a>
## [NVIDIA Nemotron-3 Embed Tops RTEB Benchmark](https://huggingface.co/blog/nvidia/nemotron-3-embed-wins-rteb) ⭐️ 8.0/10

NVIDIA's Nemotron-3 Embed model has achieved the #1 overall ranking on the RTEB (Retrieval-focused Text Embedding Benchmark), surpassing all other models in retrieval accuracy. This marks a new state-of-the-art for agentic retrieval tasks. This advancement directly improves the quality of retrieval-augmented generation (RAG) and AI agent systems, which rely on accurate information retrieval. As agentic retrieval becomes critical for enterprise AI, Nemotron-3 Embed sets a new performance standard. Nemotron-3 Embed is based on the Ministral-3-8B architecture and produces 4096-dimensional dense vectors for multilingual text. The model is available on Hugging Face and through NVIDIA NIM for deployment.

rss · Hugging Face Blog · Jul 16, 16:01

**Background**: RTEB is a new benchmark designed to evaluate retrieval accuracy of embedding models and rerankers, using a mix of open and private datasets to prevent overfitting. Agentic retrieval extends traditional search by enabling multi-step reasoning and self-correction, making it essential for advanced AI agents. Embedding models like Nemotron-3 convert text into numerical vectors that capture semantic meaning, enabling efficient similarity search.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/rteb">Introducing RTEB : A New Standard for Retrieval Evaluation</a></li>
<li><a href="https://github.com/embedding-benchmark/rteb">GitHub - embedding- benchmark / rteb : Retrieval Embedding Benchmark</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#embedding models`, `#agentic retrieval`, `#RTEB`, `#AI/ML`

---

<a id="item-8"></a>
## [Hugging Face Discloses July 2026 Security Incident](https://huggingface.co/blog/security-incident-july-2026) ⭐️ 8.0/10

Hugging Face published a blog post disclosing a security incident that occurred in July 2026, detailing the nature of the breach and its impact on users. This disclosure is critical for the AI/ML community as Hugging Face is a central platform for model hosting and collaboration, and the incident may affect user trust and security practices. The blog post provides authoritative details on the incident, including the timeline, affected systems, and remediation steps taken by Hugging Face.

rss · Hugging Face Blog · Jul 16, 00:00

**Background**: Hugging Face is a popular platform for hosting machine learning models and datasets, widely used by researchers and developers. Security incidents on such platforms can expose sensitive data or compromise model integrity.

**Tags**: `#security`, `#incident disclosure`, `#Hugging Face`, `#AI/ML platform`, `#vulnerability`

---

