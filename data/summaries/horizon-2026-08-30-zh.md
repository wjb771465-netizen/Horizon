# Horizon 每日速递 - 2026-08-30

> 从 98 条内容中筛选出 2 条重要资讯。

---

**科技新闻**
1. [OpenAI 因 SpaceX 收购 Cursor 终止模型服务](#item-tech-news-1) ⭐️ 9.0/10
2. [百年算法击败 SOTA 时间序列异常检测方法](#item-tech-news-2) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [OpenAI 因 SpaceX 收购 Cursor 终止模型服务](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 9.0/10

OpenAI 宣布因 SpaceX 收购代码编辑器 Cursor，将终止向其提供 OpenAI 模型的合同，并设定建议停服日期为 2026 年 11 月 12 日。OpenAI 表示无法确信 SpaceX 会遵守服务条款，理由是埃隆·马斯克旗下公司存在违约记录，包括收购 Twitter 后违反合同以及 xAI 今年早些时候在宣誓下承认违反 OpenAI 服务条款。双方此前已合作近四年，该定制协议允许在控制权变更后限时取消合作，OpenAI 此次给出了合同允许的最大通知期。

telegram · zaihuapd · 8月29日 02:24

**「背景」** Cursor 是一款广受欢迎的 AI 代码编辑器，此前与 OpenAI 建立了近四年的合作关系，通过定制协议直接集成 OpenAI 的模型。此次合作终止的导火索是 SpaceX 收购了 Cursor，触发了合同中关于控制权变更的条款。OpenAI 决定终止合作的主要依据是埃隆·马斯克旗下公司过往的违约记录，包括收购 Twitter 后切断 OpenAI 数据访问，以及 xAI 今年早些时候在宣誓下承认利用 OpenAI 的输出训练其 Grok 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/">Our decision on Cursor following its acquisition by SpaceX | OpenAI</a></li>
<li><a href="https://thesiliconreview.com/2026/08/openai-cuts-off-spacex-cursor-ai-models-musk-feud">OpenAI to Cut Off AI Models for SpaceX-Owned Cursor, Escalating Feud with Musk, November 12 Shutoff Date Set</a></li>
<li><a href="https://www.businessinsider.com/openai-ends-cursor-contract-elon-musk-spacex-sam-altman-feud-2026-8">OpenAI Ending Deal With Cursor Because XAI Violated Terms of Service - Business Insider</a></li>
<li><a href="https://time.news/openai-to-cut-ties-with-cursor-over-elon-musks-history-of-contract-violations/">OpenAI to Cut Ties With Cursor Over Elon Musk&#x27;s History of Contract Violations - Time News</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#SpaceX`, `#Cursor`, `#AI Models`, `#Business`

---

<a id="item-tech-news-2"></a>
### [百年算法击败 SOTA 时间序列异常检测方法](https://www.reddit.com/r/MachineLearning/comments/1w1wt1s/you_can_beat_sota_time_series_anomaly_detection/) ⭐️ 8.0/10

研究人员发现，拥有百年历史的简单统计过程控制（SPC）算法在广泛使用的 TSB-AD-M 基准测试中，其表现优于现代最先进的（SOTA）时间序列异常检测（TSAD）方法。作者指出，在大多数测试案例中，SPC 能够击败 SOTA 方法，并在附带的 ECG 轨迹示例中取得了完美结果。这一发现表明 TSB-AD 基准测试过于简单，无法对算法性能进行有意义的评估，从而质疑了过去十年该领域研究进展的真实性。作者呼吁社区对基准测试质量进行反思，并已着手引入包括雪橇犬、金枪鱼、燃料电池和智能制造在内的更具挑战性的 TSAD 问题。

reddit · r/MachineLearning · /u/eamonnkeogh · 8月29日 20:16

**「背景」** TSB-AD-M 是由 Paparrizos 等人提出的单变量时间序列异常检测基准套件，被广泛用于评估 NeurIPS 等顶级会议中的最新算法。统计过程控制（SPC）是一种拥有百年历史的统计方法，通常利用控制图来监控过程输出并检测偏离标准参数的显著偏差。该文作者指出，这种传统技术在 TSB-AD-M 基准上的表现优于现代最先进方法，从而引发了对该基准有效性的质疑。

**「影响」** 研究人员和从业者可能会重新评估在 TSB-AD-M 基准上报告的 SOTA 时间序列异常检测方法的有效性，因为简单的统计过程控制（SPC）算法已被证明能超越这些现代方法。这一发现表明，该基准过于简单，无法提供有意义的算法性能评估，可能导致过去十年的研究进展被视为一种错觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thedatumorg.github.io/TSB-AD/">TSB-AD</a></li>
<li><a href="https://www.vldb.org/pvldb/vol15/p1697-paparrizos.pdf">TSB-UAD: An End-to-End Benchmark Suite for Univariate ...</a></li>
<li><a href="https://www.linkedin.com/pulse/advanced-techniques-practical-aspects-anomaly-time-series-calledda-dxj7e">Advanced Techniques and Practical Aspects in Anomaly Detection for...</a></li>
<li><a href="https://ar5iv.labs.arxiv.org/html/1708.02635">[1708.02635] Anomaly Detection in Multivariate Non-stationary Time ...</a></li>
<li><a href="https://arxiv.org/pdf/2009.13807">Current Time Series Anomaly Detection Benchmarks are Flawed and...</a></li>
<li><a href="https://github.com/TheDatumOrg/TSB-AD">GitHub - thedatumorg/ TSB - AD : Time-Series Anomaly Detection</a></li>

</ul>
</details>

**标签**: `#Time Series Analysis`, `#Anomaly Detection`, `#Benchmark Evaluation`, `#Machine Learning Research`, `#Statistical Process Control`

---

