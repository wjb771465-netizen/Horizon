# Horizon Daily - 2026-07-10

> From 26 items, 5 important content pieces were selected

---

1. [QuadRF: Open-Source RF Camera Sees WiFi Through Walls](#item-1) ⭐️ 8.0/10
2. [GPT-5.6 Sol Ultra Claims Proof of Cycle Double Cover Conjecture](#item-2) ⭐️ 8.0/10
3. [Emacs Architecture: Everything Looks Like a Service](#item-3) ⭐️ 8.0/10
4. [How Successful Companies Go Blind to Innovation](#item-4) ⭐️ 8.0/10
5. [Profiling Attention in PyTorch: A Deep Dive](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [QuadRF: Open-Source RF Camera Sees WiFi Through Walls](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/) ⭐️ 8.0/10

Jeff Geerling reviewed QuadRF, an open-source RF sensing platform that uses a Raspberry Pi 5 and phased-array antennas to visualize WiFi signals and detect drones through walls in real time. This platform democratizes advanced RF sensing, enabling hobbyists and researchers to explore applications like drone detection, through-wall imaging, and antenna characterization, while raising important privacy concerns. QuadRF combines a Raspberry Pi 5 with four software-defined radio (SDR) channels and a phased-array antenna to create a real-time RF camera, with open-source software for augmented reality visualization.

hackernews · speckx · Jul 10, 15:59 · [Discussion](https://news.ycombinator.com/item?id=48861717)

**Background**: RF sensing uses radio waves to detect objects and movement, similar to radar. While through-wall imaging has been possible with specialized equipment, QuadRF brings this capability to an affordable, open-source platform using off-the-shelf components like the Raspberry Pi 5.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hackster.io/news/quadrf-the-open-source-rf-camera-that-lets-you-see-wi-fi-signals-141ad91f2a2d">QuadRF: The Open Source RF Camera That Lets You See Wi-Fi Signals</a></li>
<li><a href="https://www.crowdsupply.com/scale-rf/quadrf">QuadRF | Crowd Supply</a></li>
<li><a href="https://www.opensourceforu.com/2026/07/rf-imaging-platform-visualises-wi-fi-signals/">RF Imaging Platform Visualises Wi-Fi Signals - Open Source For You</a></li>

</ul>
</details>

**Discussion**: The QuadRF creator actively engaged in the discussion, answering technical questions and noting that the UI is being improved based on feedback. Commenters expressed interest in building similar systems for sound localization and speculated about government surveillance capabilities.

**Tags**: `#RF sensing`, `#open-source hardware`, `#drone detection`, `#WiFi visualization`, `#privacy`

---

<a id="item-2"></a>
## [GPT-5.6 Sol Ultra Claims Proof of Cycle Double Cover Conjecture](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf) ⭐️ 8.0/10

OpenAI's GPT-5.6 Sol Ultra model has produced a purported proof of the Cycle Double Cover Conjecture, a long-standing open problem in graph theory, released as a preprint on July 10, 2026. If verified, this would mark the first time an AI has autonomously proven a major open mathematical conjecture, potentially transforming how mathematical research is conducted and accelerating discovery. The proof is extremely concise, suggesting it exploits a clever trick previously missed by experts, and the full prompt used to generate the proof has been released, allowing scrutiny and reproducibility.

hackernews · scrlk · Jul 10, 18:29 · [Discussion](https://news.ycombinator.com/item?id=48863490)

**Background**: The Cycle Double Cover Conjecture, posed by Tutte, Itai, Rodeh, Szekeres, and Seymour, asks whether every bridgeless undirected graph has a collection of cycles covering each edge exactly twice. GPT-5.6 Sol Ultra is OpenAI's latest model, featuring an 'ultra' mode that coordinates multiple agents for complex tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cycle_double_cover_conjecture">Cycle double cover conjecture</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**Discussion**: The community is highly engaged but skeptical; many commenters note the proof's brevity and question its novelty, suggesting it may rely on a known trick. Some are impressed by the AI's ability to produce a proof at all, while others call for rigorous verification.

**Tags**: `#AI`, `#mathematics`, `#proof`, `#GPT-5.6`, `#OpenAI`

---

<a id="item-3"></a>
## [Emacs Architecture: Everything Looks Like a Service](http://yummymelon.com/devnull/in-emacs-everything-looks-like-a-service.html) ⭐️ 8.0/10

An article argues that Emacs' architecture treats external tools and processes as services, predating and paralleling modern client-server paradigms like LSP. This perspective helps developers understand Emacs' design philosophy and its relevance to modern tooling, highlighting that LSP is not a novel concept but a standardization of existing patterns. Emacs has long supported long-running subprocesses, RPC-like interactions, TRAMP, GUD, and REPL integration, all of which embody a service-oriented approach.

hackernews · kickingvegas · Jul 10, 08:21 · [Discussion](https://news.ycombinator.com/item?id=48857230)

**Background**: Emacs is a highly extensible text editor with a built-in Lisp interpreter. Its architecture allows it to orchestrate external programs, similar to an operating system. The Language Server Protocol (LSP) is a modern standard for providing language-specific features in editors, but Emacs had similar capabilities long before LSP.

<details><summary>References</summary>
<ul>
<li><a href="http://yummymelon.com/devnull/in-emacs-everything-looks-like-a-service.html">nfdn: In Emacs, Everything Looks Like a Service</a></li>
<li><a href="https://www.singletonlife.com/posts/emacs_server_and_client/">Emacs as server and client · SingletonLife</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lisp_machine">Lisp machine - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters note that Emacs' service-oriented approach predates LSP, with some arguing that the client-server dichotomy can be stretched to fit anything. Others lament workplace restrictions preventing Emacs use, despite its efficiency.

**Tags**: `#Emacs`, `#LSP`, `#software architecture`, `#client-server`, `#Lisp machines`

---

<a id="item-4"></a>
## [How Successful Companies Go Blind to Innovation](https://ianreppel.org/how-successful-companies-go-blind/) ⭐️ 8.0/10

An article by Ian Reppel analyzes how successful companies become blind to innovation due to bureaucracy, risk aversion, and internal stagnation, with community comments providing real-world validation. This analysis is significant because it highlights a common organizational trap that can stifle growth and competitiveness, affecting employees, managers, and investors across industries. The article scores 8.0/10 with 177 points and 62 comments, indicating strong community engagement. Commenters share personal experiences from defense companies, startups, and large corporations, validating the article's observations.

hackernews · speckx · Jul 10, 13:31 · [Discussion](https://news.ycombinator.com/item?id=48859678)

**Background**: Organizational blindness refers to a company's inability to recognize or act on new opportunities due to internal barriers like bureaucracy and risk aversion. Successful companies often develop these barriers over time as they grow, prioritizing stability over innovation.

**Discussion**: Commenters largely agree with the article, sharing personal anecdotes. One notes that momentum, not just blindness, is a factor, while another distinguishes between competence and context issues. A third points to VC-funded MVP culture as a contributor.

**Tags**: `#organizational culture`, `#bureaucracy`, `#innovation`, `#company growth`, `#management`

---

<a id="item-5"></a>
## [Profiling Attention in PyTorch: A Deep Dive](https://huggingface.co/blog/torch-attention-profile) ⭐️ 8.0/10

A new blog post on Hugging Face provides detailed guidance on profiling attention mechanisms in PyTorch, covering tools like PyTorch Profiler and techniques to optimize performance. Attention mechanisms are a performance bottleneck in modern deep learning models; this guide helps developers identify and resolve inefficiencies, leading to faster training and inference. The post is part of a series on PyTorch profiling and focuses on attention-specific optimizations, such as using FlexAttention and flash attention. It likely includes practical code examples and trace analysis.

rss · Hugging Face Blog · Jul 10, 00:00

**Background**: Profiling is the process of measuring where time and memory are spent in code. PyTorch Profiler is a built-in tool that collects performance metrics during training and inference. Attention mechanisms, while powerful, are computationally expensive and often become the main bottleneck in transformer models.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html">PyTorch Profiler — PyTorch Tutorials 2.13.0+cu130 documentation</a></li>
<li><a href="https://docs.pytorch.org/docs/2.12/profiler.html">torch. profiler — PyTorch 2.12 documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)">Attention (machine learning) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#PyTorch`, `#Profiling`, `#Attention`, `#Performance Optimization`, `#Deep Learning`

---

