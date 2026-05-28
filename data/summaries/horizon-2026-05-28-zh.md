# Horizon 每日速递 - 2026-05-28

> From 18 items, 4 important content pieces were selected

---

1. [Anthropic 以 9650 亿美元估值完成 650 亿美元 H 轮融资](#item-1) ⭐️ 10.0/10
2. [PostgreSQL 作为持久化工作流的完整基础](#item-2) ⭐️ 8.0/10
3. [欧盟因非法产品销售对 Temu 罚款 2 亿欧元](#item-3) ⭐️ 8.0/10
4. [SQLite 新增 AGENTS.md 文件，禁止 AI 代理代码贡献](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 以 9650 亿美元估值完成 650 亿美元 H 轮融资](https://www.anthropic.com/news/series-h) ⭐️ 10.0/10

Anthropic 宣布完成 650 亿美元的 H 轮融资，投后估值达 9650 亿美元，同时报告其年化运行收入达到 470 亿美元，在收入和估值上均超越 OpenAI。 这是历史上规模最大的私募融资轮之一，标志着 AI 行业的重大转变——Anthropic 在收入和估值上超越 OpenAI 成为领先的私营 AI 公司，可能重塑竞争格局和投资者信心。 此轮 H 轮融资紧随 2026 年 2 月的 G 轮融资，公司自报的年化运行收入在 2026 年 5 月初突破 470 亿美元，较此前的约 90 亿美元大幅增长。9650 亿美元的估值距离万亿美元仅一步之遥，使 Anthropic 几乎成为“千角兽”。

hackernews · meetpateltech · May 28, 18:09 · [社区讨论](https://news.ycombinator.com/item?id=48313048)

**背景**: Anthropic 是一家以 AI 安全与研究闻名的公司，其核心产品是 Claude 系列大语言模型。H 轮融资是面向接近 IPO 的成熟初创公司的后期融资轮。年化运行收入是将当前月度收入外推至全年的一种估算方式，常被高速增长的私营公司用于展示增长趋势。

**社区讨论**: 社区评论聚焦于与 OpenAI 的收入对比，有用户指出 Anthropic 470 亿美元的年化运行收入已超过 OpenAI 的报告数字。另一位评论者质疑年化运行收入的定义，其他人则讨论如此高的私募估值在上市前的影响，有人称 Anthropic 接近“千角兽”（独角兽为 10 亿美元）。

**标签**: `#Anthropic`, `#funding`, `#AI`, `#valuation`, `#venture capital`

---

<a id="item-2"></a>
## [PostgreSQL 作为持久化工作流的完整基础](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

DBOS 的一篇博客文章认为，仅凭 PostgreSQL 就可以作为构建持久化工作流系统的完整基础，无需单独的队列或状态机服务。 这种方法通过将数据存储、队列和工作流执行整合到单个数据库中，简化了后端架构，降低了运维复杂性和潜在的一致性问题。 文章重点介绍了诸如事务性发件箱模式和 SKIP LOCKED 等技术，用于直接在 Postgres 中实现队列，并引用了 Armin Ronacher 的'absurd'库等现有实现。

hackernews · KraftyOne · May 28, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48313530)

**背景**: 持久化工作流需要可靠的执行保证，通常依赖单独的队列系统（如 SQS）和状态机。PostgreSQL 凭借事务、咨询锁和 SKIP LOCKED 等功能，可以原生支持这些模式，从而降低架构复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html">Transactional outbox pattern - AWS Prescriptive Guidance</a></li>
<li><a href="https://neon.com/guides/queue-system">Queue System using SKIP LOCKED in Neon Postgres - Neon Guides</a></li>
<li><a href="https://news.ycombinator.com/item?id=20020501">I use Postgres SKIP LOCKED as a queue. I used to use SQS but Postgres gives me e... | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论通过实际经验验证了这种方法：用户分享了他们自己使用 Postgres 作为队列和工作流引擎的实现，并提到了'absurd'等替代库。一些人指出，虽然 Postgres 在低到中等规模下表现良好，但在非常大的规模下可能需要专门的系统。

**标签**: `#PostgreSQL`, `#durable workflows`, `#backend engineering`, `#distributed systems`, `#queue management`

---

<a id="item-3"></a>
## [欧盟因非法产品销售对 Temu 罚款 2 亿欧元](https://www.bbc.co.uk/news/articles/c1k2ydn1rz8o) ⭐️ 8.0/10

欧盟因 Temu 平台允许销售非法产品，对其处以 2 亿欧元罚款，理由是违反了《数字服务法案》（DSA）。 此次罚款表明欧盟正在积极执行平台责任规则，可能迫使 Temu 等低价电商平台加强产品审查，否则将面临严厉处罚。 罚款依据是《数字服务法案》，该法案要求平台主动移除非法商品。Temu 尚未就是否上诉发表评论。

hackernews · jjp · May 28, 14:18 · [社区讨论](https://news.ycombinator.com/item?id=48309302)

**背景**: 欧盟的《数字服务法案》（DSA）自 2024 年起生效，对在线市场上第三方卖家销售的非法内容和产品施加严格责任。Temu 是一家以超低价著称的中国电商平台，此前已因假冒伪劣和不安全商品受到审查。这是迄今为止 DSA 下最大的一笔罚款之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digital-strategy.ec.europa.eu/en/policies/digital-services-act">The Digital Services Act | Shaping Europe’s digital future</a></li>
<li><a href="https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AA3D55C57B0F6A7C18F5CAEF25146557/9781009438629c3_20-40.pdf/platform_responsibility_in_the_european_union.pdf">Platform Responsibility in the European Union</a></li>
<li><a href="https://www.wisemen.nl/en/news/the-new-platform-liability-from-the-e-commerce-directive-to-the-digital-services-act-regulation-dsa-/">The New Platform Liability: from the e-Commerce Directive to ...</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人认为 Temu 满足了人们对廉价商品的实际需求，而另一些人则质疑为何亚马逊和 eBay 没有受到类似处罚。还有评论指出，对中国平台的执法如同“打地鼠”般困难。

**标签**: `#EU regulation`, `#e-commerce`, `#Temu`, `#platform liability`, `#consumer protection`

---

<a id="item-4"></a>
## [SQLite 新增 AGENTS.md 文件，禁止 AI 代理代码贡献](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite 新增了 AGENTS.md 文件，明确声明不接受 AI 代理生成的代码贡献，但欢迎 bug 报告和文档补丁。该政策通过移除“currently”一词得到强化，同时 SQLite 还创建了专门的 Bug 论坛来处理 AI 生成的 bug 报告。 这为正在应对 AI 生成贡献的开源项目树立了明确先例，解决了质量和法律方面的担忧。它可能促使其他项目采取类似政策，以保护其代码库免受低质量或法律模糊的代理代码的影响。 AGENTS.md 文件还指出，人类开发者会将写得好的 pull request 作为概念验证进行审查，但会自行重新实现更改。最近的提交移除了“currently”一词以强化立场，而 SQLite 论坛曾被 AI 生成的 bug 报告淹没，因此创建了专门的 bug 论坛。

rss · Simon Willison · May 27, 23:44

**背景**: Agentic coding（代理编码）是一种软件开发方法，其中自主 AI 代理在最少人工干预下规划、编写、测试和修改代码，不同于等待用户输入的传统 AI 助手。这些代理可能引入与项目标准或法律要求相冲突的设计决策，引发开源维护者的担忧。SQLite 的政策明确拒绝此类代理代码，同时仍允许人类贡献和 bug 报告，反映了围绕 AI 生成贡献的治理需求日益增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is Agentic Coding? | IBM</a></li>
<li><a href="https://apiiro.com/glossary/agentic-coding/">What Is Agentic Coding? Risks & Best Practices</a></li>

</ul>
</details>

**标签**: `#sqlite`, `#AI agents`, `#open-source governance`, `#software engineering`, `#policy`

---

