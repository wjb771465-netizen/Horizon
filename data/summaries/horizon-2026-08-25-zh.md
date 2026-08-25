# Horizon 每日速递 - 2026-08-25

> 从 108 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [seL4 在 AArch64 上的安全证明完成](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [seL4 在 AArch64 上的安全证明完成](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核的安全证明已在 AArch64 架构上完成，这是形式化验证领域的一个重要里程碑。该成果由 Proofcraft Systems 于 2026-08-21 发布，意味着 seL4 的机密性、完整性等安全属性在 AArch64 上获得了机器可验证的证明。不过社区提醒，当前证明复盖的是非 MCS（混合关键性系统）和单核配置，并不包含多核或 MCS 扩展。这一进展对安全关键型部署有直接意义，但实际采用仍受限于生态成熟度以及与 Linux 兼容性等问题。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是一个以能力（capability）机制实现访问控制的微内核，其安全模型通过形式化验证来保证内核的保密性等安全属性。这些证明使用 Isabelle/HOL 定理证明器编写，并托管在 seL4/l4v 仓库中，针对特定版本和配置的 seL4 进行验证。此次完成的是 AArch64（64 位 ARM 架构）上的保密性证明，意味着在该架构上，运行于 seL4 之上的应用程序被数学上证明无法未经授权获取信息。

**「影响」** 对在 AArch64 上部署 seL4 的开发者和机构而言，安全证明的完成意味着 64 位 ARM 平台现在也获得了与先前架构相当的形式化安全保证，可进一步支撑汽车、军事和嵌入式等高可信场景的采用。需要明确的是，这些证明复盖的是非 MCS（混合关键性系统）的单核配置，多核与 MCS 配置仍不在证明范围内；同时，seL4 基金会也指出大多数实际部署并不会全部原生运行在 seL4 上，因此实际安全收益仍取决于整体系统集成。

**「社区讨论」** 评论中既有对成果的认可，也提出保留意见：有观点认为侧信道时序攻击可能使该结果失效；另有人提醒细则限定于非 MCS、单核配置。还有讨论关注实际使用 seL4 的操作系统（如 GenodeOS、LionsOS、某中国车企的 hypervisor），以及是否需要原生 seL4/Linux 才能宣称改善系统安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
<li><a href="https://sel4.systems/Verification/proofs.html">seL4 Proofs | seL4</a></li>
<li><a href="https://docs.sel4.systems/projects/sel4/verified-configurations.html">Verified Configurations | seL4 docs</a></li>
<li><a href="https://sel4.systems/About/seL4-whitepaper.pdf">The seL4® Foundation https://sel4.systems/Foundation The seL4 Microkernel</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>

</ul>
</details>

**标签**: `#seL4`, `#formal verification`, `#microkernel`, `#AArch64`, `#security`

---

