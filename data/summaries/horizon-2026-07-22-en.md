# Horizon Daily - 2026-07-22

> From 16 items, 4 important content pieces were selected

---

1. [Terrence Tao Uses ChatGPT to Explore Jacobian Conjecture](#item-1) ⭐️ 8.0/10
2. [Bento: Full slide editor in a single offline HTML file](#item-2) ⭐️ 8.0/10
3. [Postgres Survival Guide for Startups](#item-3) ⭐️ 8.0/10
4. [Take-Home Interview Project Hides Malicious Git Hook](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Terrence Tao Uses ChatGPT to Explore Jacobian Conjecture](https://chatgpt.com/share/6a5fdc7a-d6f8-83e8-bbea-8deb42cfed56) ⭐️ 8.0/10

Terrence Tao shared a ChatGPT conversation where he used the AI to explore a counterexample to the Jacobian conjecture, demonstrating advanced AI-assisted mathematical reasoning. The conversation shows Tao asking precise questions to guide the model through complex algebraic geometry concepts. This marks a significant demonstration of how large language models can assist top mathematicians in research, potentially accelerating discovery and collaboration. It also highlights the evolving role of AI in formal reasoning and problem-solving within mathematics. The counterexample was discovered by Levent Alpöge in July 2026 using Claude Fable 5, disproving the Jacobian conjecture for dimensions greater than 2. Tao's conversation shows him using ChatGPT to verify and understand the structure of the polynomial counterexample.

hackernews · gmays · Jul 22, 17:30 · [Discussion](https://news.ycombinator.com/item?id=49010345)

**Background**: The Jacobian conjecture is a long-standing problem in algebraic geometry stating that a polynomial map with a nonzero constant Jacobian determinant must have a polynomial inverse. It was first stated for two variables in 1884 and later generalized, but remained open for over a century despite many attempted proofs. Terrence Tao is a Fields Medal-winning mathematician known for his work across multiple areas of mathematics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jacobian_conjecture">Jacobian conjecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao</a></li>

</ul>
</details>

**Discussion**: Commenters were fascinated by Tao's expert use of ChatGPT, noting how his precise questioning and deep domain knowledge allowed him to extract valuable insights. Some highlighted that the counterexample was not brute-forced but structurally significant, and that Tao's interaction pattern mirrors how experts can leverage LLMs effectively.

**Tags**: `#mathematics`, `#AI`, `#ChatGPT`, `#research`, `#LLM`

---

<a id="item-2"></a>
## [Bento: Full slide editor in a single offline HTML file](https://bento.page/slides/) ⭐️ 8.0/10

Bento is a single HTML file (~560 KB) that contains a complete slide editor with animations, real-time collaboration, and offline functionality, requiring no installation or cloud login. This demonstrates a new paradigm for local-first, portable applications that can be easily shared and edited without relying on cloud services, potentially reducing dependency on large presentation tools. The file uses a JSON block for slide data and a base64-encoded app blob that is decompressed in the browser via DecompressionStream, keeping the package small. Collaboration is achieved through an encrypted blind relay that does not see the data.

hackernews · starfallg · Jul 22, 15:19 · [Discussion](https://news.ycombinator.com/item?id=49008211)

**Background**: Traditional slide editors like PowerPoint or Google Slides require installation or cloud connectivity. Single-file web applications bundle all resources into one HTML file, enabling offline use and easy distribution. Local-first architecture prioritizes client-side data and offline capability, reducing reliance on servers.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Single-File_HTML_Utilities">Single-File HTML Utilities</a></li>
<li><a href="https://techbuzzonline.com/local-first-software-architecture-guide/">Local-First Software Architecture: Beginner’s Guide to ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News community praised Bento's innovation, with the creator explaining its architecture. Some users noted performance issues under heavy concurrent editing, and others discussed the broader trend of local-first software and single-file apps.

**Tags**: `#presentation-tools`, `#single-file-app`, `#offline-first`, `#web-development`, `#local-first`

---

<a id="item-3"></a>
## [Postgres Survival Guide for Startups](https://hatchet.run/blog/postgres-survival-guide) ⭐️ 8.0/10

A practical guide for startups using PostgreSQL has been published, covering common pitfalls and best practices for scaling and maintaining databases. This guide addresses critical issues that many startups face as they grow, helping them avoid costly mistakes and improve database reliability. The guide includes advice on using UUIDv7 instead of UUIDv4, ordering locks deterministically to avoid deadlocks, and using EXPLAIN (GENERIC_PLAN) for query analysis.

hackernews · abelanger · Jul 22, 12:36 · [Discussion](https://news.ycombinator.com/item?id=49005787)

**Background**: PostgreSQL is a popular open-source relational database used by many startups. As data grows, common issues like slow queries, deadlocks, and backup failures can threaten operations. This guide aims to provide actionable solutions.

**Discussion**: Commenters highlighted missing topics like backup strategies and recommended tools such as Barman. They also debated the use of ORMs, cascading deletes, and append-only patterns, offering additional insights and corrections.

**Tags**: `#PostgreSQL`, `#startups`, `#database`, `#best practices`, `#scaling`

---

<a id="item-4"></a>
## [Take-Home Interview Project Hides Malicious Git Hook](https://citizendot.github.io/articles/fake-job-interview-git-hook-malware/) ⭐️ 8.0/10

A security researcher discovered that a take-home coding assessment contained a malicious Git hook that silently executed a remote payload, marking a novel attack vector in the hiring process. This incident highlights a growing trend of supply chain attacks targeting developers through seemingly legitimate interview tasks, posing risks to both job seekers and companies. The malicious hook checked the victim's operating system and used a raw IP address to fetch a payload, which could have led to remote code execution on the developer's machine.

hackernews · CITIZENDOT · Jul 22, 20:33 · [Discussion](https://news.ycombinator.com/item?id=49013036)

**Background**: Git hooks are scripts that run automatically at certain points in Git's workflow, such as before a commit. Attackers can embed malicious hooks in repositories to execute arbitrary code when a developer performs common Git operations.

<details><summary>References</summary>
<ul>
<li><a href="https://sscsecurity.dev/book1/chapter-08/ch-8.5/">Git -Specific Attack Vectors - Open Source Software Supply Chain...</a></li>
<li><a href="https://github.com/muasif80/git-hook-guard">GitHub - muasif80/ git - hook -guard: Auto-scans opened Git repositories...</a></li>
<li><a href="https://www.invicti.com/learn/remote-code-execution-rce">Remote Code Execution (RCE)</a></li>

</ul>
</details>

**Discussion**: Commenters noted that this attack vector is becoming a recurring theme, with a similar story on Hacker News last month. Some criticized the use of a raw IP address as a telltale sign of malware, while others debated whether Claude's safety safeguards hindered its usefulness as a helper.

**Tags**: `#malware`, `#security`, `#git`, `#interview`, `#supply chain attack`

---

