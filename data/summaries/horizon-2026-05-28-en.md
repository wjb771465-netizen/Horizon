# Horizon Daily - 2026-05-28

> From 18 items, 4 important content pieces were selected

---

1. [Anthropic raises $65B in Series H at $965B valuation](#item-1) ⭐️ 10.0/10
2. [PostgreSQL as a Complete Foundation for Durable Workflows](#item-2) ⭐️ 8.0/10
3. [EU fines Temu €200M for illegal product sales](#item-3) ⭐️ 8.0/10
4. [SQLite Bans Agentic Code Contributions with New AGENTS.md Policy](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic raises $65B in Series H at $965B valuation](https://www.anthropic.com/news/series-h) ⭐️ 10.0/10

Anthropic announced a $65 billion Series H funding round at a $965 billion post-money valuation, and reported a run-rate revenue of $47 billion, surpassing OpenAI in both revenue and valuation. This is one of the largest private funding rounds in history, signaling a major shift in the AI industry as Anthropic overtakes OpenAI as the leading private AI company by revenue and valuation, which could reshape competitive dynamics and investor confidence. The Series H round follows a Series G in February 2026, and the company's self-reported run-rate revenue crossed $47 billion in early May 2026, up from approximately $9 billion earlier. The valuation of $965 billion is just shy of a trillion dollars, making Anthropic nearly a 'kilocorn'.

hackernews · meetpateltech · May 28, 18:09 · [Discussion](https://news.ycombinator.com/item?id=48313048)

**Background**: Anthropic is an AI safety and research company best known for its Claude family of large language models. Series H is a late-stage funding round typically reserved for mature startups approaching an IPO. Run-rate revenue is an extrapolation of current monthly revenue to estimate annual revenue, often used by fast-growing private companies to indicate growth trajectory.

**Discussion**: Community comments highlight the revenue comparison with OpenAI, with one user noting Anthropic's run-rate revenue of $47 billion surpasses OpenAI's reported figures. Another commenter questions the definition of run-rate revenue, while others discuss the implications of such high private valuations before going public, with some calling Anthropic a near 'kilocorn' (a unicorn being $1 billion).

**Tags**: `#Anthropic`, `#funding`, `#AI`, `#valuation`, `#venture capital`

---

<a id="item-2"></a>
## [PostgreSQL as a Complete Foundation for Durable Workflows](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

A blog post from DBOS argues that PostgreSQL alone can serve as a complete foundation for building durable workflow systems, eliminating the need for separate queue or state machine services. This approach simplifies backend architecture by consolidating data storage, queuing, and workflow execution into a single database, reducing operational complexity and potential consistency issues. The post highlights techniques like the transactional outbox pattern and SKIP LOCKED for implementing queues directly in Postgres, and references existing implementations such as Armin Ronacher's 'absurd' library.

hackernews · KraftyOne · May 28, 18:41 · [Discussion](https://news.ycombinator.com/item?id=48313530)

**Background**: Durable workflows require reliable execution guarantees, often relying on separate queue systems (e.g., SQS) and state machines. PostgreSQL, with features like transactions, advisory locks, and SKIP LOCKED, can natively support these patterns, reducing architectural complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html">Transactional outbox pattern - AWS Prescriptive Guidance</a></li>
<li><a href="https://neon.com/guides/queue-system">Queue System using SKIP LOCKED in Neon Postgres - Neon Guides</a></li>
<li><a href="https://news.ycombinator.com/item?id=20020501">I use Postgres SKIP LOCKED as a queue. I used to use SQS but Postgres gives me e... | Hacker News</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion validates the approach with practical experiences: users share their own implementations using Postgres as a queue and workflow engine, and point to alternative libraries like 'absurd'. Some note that while Postgres works well at low to moderate scale, specialized systems may be needed at very large scale.

**Tags**: `#PostgreSQL`, `#durable workflows`, `#backend engineering`, `#distributed systems`, `#queue management`

---

<a id="item-3"></a>
## [EU fines Temu €200M for illegal product sales](https://www.bbc.co.uk/news/articles/c1k2ydn1rz8o) ⭐️ 8.0/10

The European Union has fined Temu €200 million for allowing the sale of illegal products on its platform, citing violations of the Digital Services Act (DSA). This fine signals the EU's aggressive enforcement of platform liability rules, potentially forcing low-cost e-commerce platforms like Temu to tighten product vetting or face severe penalties. The fine is based on the DSA, which requires platforms to proactively remove illegal goods. Temu has not yet commented on whether it will appeal.

hackernews · jjp · May 28, 14:18 · [Discussion](https://news.ycombinator.com/item?id=48309302)

**Background**: The EU's Digital Services Act (DSA), effective since 2024, imposes strict liability on online marketplaces for illegal content and products sold by third-party sellers. Temu, a Chinese-owned e-commerce platform known for ultra-low prices, has faced scrutiny over counterfeit and unsafe goods. This is one of the largest fines under the DSA to date.

<details><summary>References</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-services-act">The Digital Services Act | Shaping Europe’s digital future</a></li>
<li><a href="https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AA3D55C57B0F6A7C18F5CAEF25146557/9781009438629c3_20-40.pdf/platform_responsibility_in_the_european_union.pdf">Platform Responsibility in the European Union</a></li>
<li><a href="https://www.wisemen.nl/en/news/the-new-platform-liability-from-the-e-commerce-directive-to-the-digital-services-act-regulation-dsa-/">The New Platform Liability: from the e-Commerce Directive to ...</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some argue Temu fills a real need for affordable goods, while others question why Amazon and eBay aren't similarly fined. Several note that enforcement against Chinese platforms is a 'whack-a-mole' challenge.

**Tags**: `#EU regulation`, `#e-commerce`, `#Temu`, `#platform liability`, `#consumer protection`

---

<a id="item-4"></a>
## [SQLite Bans Agentic Code Contributions with New AGENTS.md Policy](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite added an AGENTS.md file explicitly stating that it does not accept agentic code contributions, while welcoming bug reports and documentation patches. The policy was strengthened by removing the word 'currently' from the statement, and SQLite also created a separate Bug Forum to handle AI-generated bug reports. This sets a clear precedent for open-source projects grappling with AI-generated contributions, addressing quality and legal concerns. It may influence other projects to adopt similar policies to protect their codebases from low-quality or legally ambiguous agentic code. The AGENTS.md file also notes that human developers will review well-written pull requests as proof-of-concept but will reimplement changes themselves. The most recent commit removed the word 'currently' to strengthen the stance, and SQLite's forum was flooded with AI-generated bug reports, leading to the creation of a dedicated bug forum.

rss · Simon Willison · May 27, 23:44

**Background**: Agentic coding is a software development approach where autonomous AI agents plan, write, test, and modify code with minimal human intervention, unlike traditional AI assistants that wait for user input. These agents can introduce design decisions that conflict with project standards or legal requirements, raising concerns for open-source maintainers. SQLite's policy explicitly rejects such agentic code while still allowing human contributions and bug reports, reflecting a growing need for governance around AI-generated contributions.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is Agentic Coding? | IBM</a></li>
<li><a href="https://apiiro.com/glossary/agentic-coding/">What Is Agentic Coding? Risks & Best Practices</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#AI agents`, `#open-source governance`, `#software engineering`, `#policy`

---

