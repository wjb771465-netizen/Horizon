# Horizon 每日速递 - 2026-08-25

> 从 134 条内容中筛选出 1 条重要资讯。

---

**科技新闻**
1. [seL4 完成 AArch64 安全证明，形式化验证里程碑](#item-tech-news-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [seL4 完成 AArch64 安全证明，形式化验证里程碑](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核的 AArch64 安全证明现已完成，这是 ARM 64 位系统形式化验证的重要进展。该成果由 Proofcraft 于 2026-08-21 发布，覆盖 AArch64 架构的安全性质，但社区指出其范围限于非 MCS（混合关键性系统）和单核（unicore）配置，且不包含侧信道时序攻击的证明。对追求高可信、形式化验证内核的开发者以及嵌入式、军事等高风险领域而言，这仍是高价值里程碑，但实际部署中仍需注意这些边界条件。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**「背景」** seL4 是一个从设计到实现都经过形式验证的微内核，其验证工作始于 2009 年发表的 SOSP 论文，涵盖功能正确性、信息流非干扰以及用户级系统初始化等证明，并可配置为分离内核以提供强隔离。官方页面显示，在 AArch64 架构上完成安全证明后，seL4 现在能以数学证明的形式保证运行于其上的应用无法在未获授权的情况下获取信息，即强制执行机密性。

**「影响」** 这一里程碑意味着，在公告所列假设下，AArch64 上运行的 seL4 实现代码现已具备正式证明的安全隔离保证，使基于 64 位 Arm 的高保证系统可以更可靠地依赖内核的隔离能力。

**「社区讨论」** 评论中有人提醒细看适用范围：当前证明针对非 MCS 与单核配置，且侧信道时序攻击可能使结果失效；另有讨论关注实际使用 seL4 的系统（如 GenodeOS、LionsOS 及某中国车企的 hypervisor 部署），并认为若想真正改善系统安全，需要原生 seL4/Linux 支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
<li><a href="https://sel4.systems/Research/pdfs/comprehensive-formal-verification-os-microkernel.pdf">2 Comprehensive Formal Veriﬁcation of an OS Microkernel</a></li>
<li><a href="https://www.sigops.org/s/conferences/sosp/2009/papers/klein-sosp09.pdf">seL4: Formal Veriﬁcation of an OS Kernel</a></li>
<li><a href="https://lists.sel4.systems/hyperkitty/list/announce@sel4.systems/thread/ZL6HYXH3PKI6XUVKMPTLIPKQMWJW7N7M/">seL 4 security proofs now complete on AArch 64 ... - lists. sel 4 . systems</a></li>

</ul>
</details>

**标签**: `#seL4`, `#formal verification`, `#AArch64`, `#microkernel`, `#security`

---

