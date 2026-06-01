# 量子计算在宏观经济与大类资产配置中的应用:研究综述(2023–2026)

> Quantum Computing in Macroeconomics and Multi-Asset / Strategic Asset Allocation: A Literature Review
>
> 整理日期:2026-06 · 用途:论文文献综述基础稿 · 方法:多源网络检索 + 对抗式交叉验证

---

## 0. 阅读指南与可信度分级

本文每条结论后标注证据等级,供撰写论文时取舍:

- **[A] 同行评审 / 权威综述**——可直接引用(如 Nature 系列、*Quantum*、IEEE、PRX Quantum)。
- **[B] 预印本 / 机构资源估计**——可引用但需标注为预印本或工程估计。
- **[C] 厂商新闻稿 / 行业媒体**——仅作"产业动态"佐证,数字多含营销成分,勿作为性能证据。
- **[!] 待核实**——日期较新(2025Q4–2026)的预印本,arXiv 编号与具体数字尚未逐一打开 PDF 核对,引用前务必复核。

> ⚠️ 检索环境中 WebFetch 对多数学术域名返回 403,部分细节依赖检索引擎摘要。三条"承重"结论(Fraunhofer 基准、HSBC/IBM、Herman 综述)已单独二次检索确认;其余 2025Q4 之后的预印本请在投稿前打开原文核对编号与数字。

---

## 1. 执行摘要(Executive Summary)

**核心判断:截至 2026 年年中,量子计算在大类资产配置与宏观分析中尚无经得起检验的"量子优势"(quantum advantage)兑现。** 现阶段的进展集中在三类:(1) 算法与可行性(workflow feasibility)的工程化演示;(2) **量子启发式经典算法**(quantum-inspired,如张量网络)带来的真实但增量的收益;(3) 容错硬件路线图的里程碑(纠错、逻辑比特),而非应用层面的金融优势。

支撑该判断的最有力证据:

1. **组合优化:经典求解器完胜。** 2025 年 9 月 Fraunhofer 的大规模基准(250 个实例、至多 1000 资产)显示,经典混合整数规划(Gurobi)在**秒级**将所有实例解到证明最优,比 QAOA / 量子退火快 1000 倍以上;在 60 秒限时内 QAOA "与随机采样无明显差异"。结论原文:"量子优势在组合优化中只有非常有限的空间"。**[A]**
2. **风险与定价:加速是二次的,且需容错硬件。** 量子振幅估计(QAE)对蒙特卡洛仅有**二次加速**(O(1/N) vs O(1/√N)),非指数级;高盛+IBM 的资源估计显示"有用"的衍生品定价需 ~7500 个逻辑比特、4600 万 T-深度、10 MHz 逻辑时钟——远超 2026 年硬件。Google 的论证更指出:**仅靠二次加速,在早期容错机上可能根本无法战胜优化过的经典蒙特卡洛**。**[A]**
3. **机器学习:理论上限+去量子化双重夹击。** 量子核方法存在"指数集中"(exponential concentration),量子神经网络存在"贫瘠高原"(barren plateaus);Tang 等的"去量子化"(dequantization)表明许多被宣称的指数级 QML 加速对低秩问题只是多项式级。生产中真正落地的(如 Itaú/QC Ware)往往是**量子启发的经典方法**,增益约 6%。**[A]**
4. **最受关注的 2025 年"首例"(HSBC/IBM 债券交易)是历史数据上的概念验证,且"优势"疑由硬件噪声贡献、未被独立复现。** **[A/C]**

**一句话给论文:** 量子计算在资产配置中目前处于"概念验证 + 量子启发式增量收益"阶段;真正的容错量子优势是 2029–2035 年的厂商目标,而非当下现实。批判性论文的最强论据是技术-定量层面的四道硬墙:**百万年级容错运行时估计、去量子化、数据加载瓶颈、贫瘠高原**。

---

## 2. 四大技术路线及其在资产配置中的应用

### 2.1 量子优化:投资组合优化(Portfolio Optimization)

将马科维茨均值-方差(mean-variance / Markowitz)及带约束(基数约束 cardinality、预算约束 budget、ESG)的组合选择,编码为 **QUBO**(二次无约束二元优化)/ Ising 模型,用以下方法求解:

| 方法 | 英文 | 硬件 | 现状 |
|---|---|---|---|
| 量子近似优化算法 | QAOA | 门模型(IBM 等) | 演示为主,易受噪声/贫瘠高原影响 |
| 量子退火 | Quantum Annealing | D-Wave | 可扩展到大变量,但非优势 |
| 变分量子本征求解器 | VQE | 门模型 | 已扩展到 ~38 资产(IBEX 35) |

**关键证据:**

- **[A] 经典完胜的基准。** Stopfer & Wagner(Fraunhofer IIS),*Quantum Portfolio Optimization: An Extensive Benchmark*,arXiv:2509.17876(2025-09)。250 实例、至多 1000 资产:Gurobi 秒级证明最优、比 SCIP 快 1000 倍;问题定制启发式在固定运行时下持续优于量子方法;**量子退火略优于 QAOA(且仅在参数精调后)**;60 秒内 QAOA ≈ 随机采样。原文结论:量子优势"空间非常有限"。→ 这是反炒作的最强锚点。
- **[A] "无明确最优"。** Mugel, Orús et al.,*Dynamic Portfolio Optimization with Real Datasets*,Phys. Rev. Research 4, 013006(2022,arXiv:2007.00017):52 资产/8 年数据,D-Wave 混合解与张量网络都能扩展到 ~1272 全连接变量,但"无法明确哪种算法/硬件最优"。
- **[B] 混合退火工作流(诚实定位)。** Morapakula et al.(Qkrishi),arXiv:2504.08843 / *Adv. Quantum Tech.*(2025):D-Wave CQM + 经典凸优化的端到端管线,**明确声明不主张量子优势**,只论证工作流可行性。
- **[B] VQE 扩展到工业规模。** arXiv:2512.22001(2025-12, [!]):通过约束分解 + Ising 采样恢复将 VQE 跑到 38 资产 IBEX 35 实盘,但无干净的"击败经典"结果。
- **[B] 约束保持技术。** XY-mixer + Dicke 态初始化可严格保持基数约束(Hamming 权重=K),避免软惩罚项扭曲能量面(arXiv:2508.13954 多类 VQE;arXiv:2602.14827 [!])。
- **[C/!] 厂商工程里程碑(非优势)。** Fujitsu 的 Pauli 关联编码(PCE)在 55 比特上跑 >250 变量、门数 <750(arXiv:2511.21305);IonQ 相关离子阱 BF-DCQO 将 250 资产分解到 36–60 比特(arXiv:2602.23976 [!])。二者均与**自选弱基线**比较,未对标 Gurobi/模拟退火,故不与上面的基准结论矛盾。
- **⚠️ 慎引:** 若干 2026 预印本报告"夏普比率击败经典"(如 QAOA-XY 夏普 1.81 vs 模拟退火 1.31,10 资产单年回测;arXiv:2602.14827 [!])——**这是小样本回测,不是计算/算法优势**,n=10、单年,统计极脆弱,勿作为量子优势证据。

### 2.2 量子机器学习:宏观预测、因子建模、情景生成

| 应用 | 代表方法 | 现状 |
|---|---|---|
| 时间序列/波动率预测 | 量子储备池计算(QRC) | 小系统上报告优于 HAR/ML 基线 [B] |
| 因子模型/信用风险 | 正交/复合层 QNN | 以**更少参数匹配**经典,非击败 [A] |
| 情景生成/合成数据 | 量子(启发)GAN(qGAN) | 能复现分布+时序相关(典型化事实)[A] |
| 宏观(GDP)预测 | QNN / SVR-量子蝙蝠算法 | 多为量子启发,核心论文早于 2024 [B] |

**关键证据:**

- **[A] 量子核方法的理论上限(反炒作锚点)。** Thanasilp, Wang, Cerezo, Holmes,*Exponential concentration in quantum kernel methods*,Nat. Commun. 15(2024,arXiv:2208.11060):量子核值随比特数指数集中,多项式次测量下退化为与输入无关的平凡模型;明确点名金融(欺诈检测)受影响。
- **[A] 生产收益来自量子启发的经典方法。** Cherrat, Kerenidis et al.(Itaú Unibanco / QC Ware),*Improved financial forecasting via QML*,*Quantum Machine Intelligence* 6(1)(2024-05,arXiv:2306.12965):量子启发的行列式点过程使流失预测精度 +~6%;QNN 以**更少参数匹配**(非超越)经典信用风险表现。作者明言:当下收益来自量子启发的经典方案。
- **[A] qGAN 情景生成。** Leiden 团队,*Quantum generative modeling for financial time series with temporal correlations*,*Mach. Learn.: Sci. Technol.*(2025,arXiv:2507.22035):量子(或张量网络模拟)生成器可同时复现目标分布与时序相关;质量依赖超参,未证明优于经典 Quant-GAN。
- **[B] 量子储备池计算。** Li et al.,*Quantum Reservoir Computing for Realized Volatility Forecasting*,Phys. Rev. Research(2025,arXiv:2505.13933):横向场 Ising QRC 预测标普 500 已实现波动率,经模型置信集(MCS)评估"持续优于"计量与 ML 基线(小系统)。
- **[B/!] 诚实的基准研究。** arXiv:2601.03802(2026-01, [!]):混合 QNN 仅在数据结构与电路设计对齐的窄区间小幅胜过**参数匹配**的经典模型;QLSTM 仅在 4 个市场状态中的 2 个胜出——"仅在结构对齐时才有增益"本身就是诚实证据。
- **[B] 宏观/GDP 预测。** Alaminos et al.,*Quantum Computing and Deep Learning Methods for GDP Growth Forecasting*,*Computational Economics* 59(2)(2022):70 国 GDP,QNN/SVR-量子蝙蝠在波动环境中占优,但核心论文早于本窗口、且"97.7% 计算时间缩减"多反映量子启发求解器而非预测精度优势。**这是最接近真正"宏观经济"QML 的工作,但偏量子启发。**
- **⚠️ 慎引:** "+72% 夏普"类单研究回测(arXiv:2512.06630 [!])、以及 Quantum Zeitgeist 之类宣传媒体的"80% 机构参与 / $622B"数字,**勿引**。

### 2.3 量子振幅估计 / 量子蒙特卡洛:风险管理与衍生品定价

这是数学上**最扎实**的方向(加速可被证明),但也是**对硬件要求最离谱**的方向。

**关键证据:**

- **[A] 基础:二次加速(非指数)。** Stamatopoulos, Egger, Woerner et al.,*Option Pricing using Quantum Computers*,*Quantum* 4, 291(2020):QAE 误差随样本数 N 以 O(1/N) 收敛,优于经典蒙特卡洛 O(1/√N)。**注意:是二次加速,很多二手资料误称"指数级",是错的。**
- **[A] 风险测度可算。** Woerner & Egger,*Quantum Risk Analysis*,npj QI(2019,arXiv:1806.06893):QAE + 对损失阈值二分搜索可算 VaR、CVaR/预期损失(Expected Shortfall),保持主项二次优势。Egger et al.,*Credit Risk Analysis using Quantum Computers*,IEEE Trans. Computers(2020):算经济资本要求(ECR=VaR−预期损失)。2024 扩展:Stamatopoulos et al. arXiv:2404.10088(衍生品 VaR/CVaR)。
- **[A] 容错门槛(承重数字)。** Chakrabarti, ..., Zeng(高盛+IBM),*A Threshold for Quantum Advantage in Derivative Pricing*,*Quantum* 5, 463(2021,arXiv:2012.03819):对 autocallable / TARF 衍生品的端到端估计——需 **~7500 逻辑比特、~4600 万 T-深度、~10 MHz 逻辑时钟**才能在 ~1 秒内击败经典。
- **[A] 优化后仍遥远。** Stamatopoulos & Zeng(高盛),*Derivative Pricing using Quantum Signal Processing*,*Quantum* 8, 1322(2024):QSP 将估计降至 **~4700 逻辑比特、10⁹ T 门、45 MHz**(T 门减 ~16×、比特减 ~4×),但仍远超现有硬件。
- **[A] 最关键的批判:二次加速可能根本不够。** Babbush, McClean et al.(Google),*Focus beyond quadratic speedups for error-corrected quantum advantage*,PRX Quantum 2, 010103(2021):纠错的常数因子开销使**仅有二次加速的算法在第一代容错机上可能永远跑不赢优化的经典蒙特卡洛**;逻辑时钟约 kHz–MHz 量级,而经典 CPU 是 GHz,存在 10³–10⁶× 的单操作惩罚,须靠极大问题规模才能摊销。
- **[C] NISQ 概念验证(谨慎)。** 摩根大通/IBM 在 127 比特 Eagle 上为欧式期权定价、宣称 ~100× 更少 shots——这是低维有利实例的 shot 数比,**非端到端运行时优势**,计入态制备与误差缓解后不成立。

### 2.4 量子启发式 / 张量网络(Quantum-Inspired / Tensor Networks)

**当下真正在金融中产生增量价值的,往往是这一类"经典"方法**(Multiverse Computing 的核心、Itaú 的生产收益、BBVA 的张量网络试验)。它们借鉴量子态表示但在经典硬件上运行,因此不受 NISQ 噪声限制——但也正因为可在经典上高效模拟,本身**不构成量子优势的证据**(参见去量子化)。

---

## 3. 机构与硬件厂商实践(2021–2026)

> 状态分级:**生产/近生产** > **真实/历史数据上的概念验证(PoC)** > **算法/资源估计研究** > **厂商营销**。**目前无一可明确称为"生产中运行"。**

| 机构 / 合作 | 应用 | 硬件/方法 | 关键数字 | 状态 | 等级 |
|---|---|---|---|---|---|
| **HSBC + IBM**(2025-09) | 算法债券交易(成交概率预测) | IBM Heron | 较经典 **+34%**;110 万笔询价、5000+ 欧洲公司债 | 历史数据 PoC;"优势"疑由硬件噪声、未独立复现 | [A/C] |
| **摩根大通 + QC Ware**(2023) | 深度对冲(deep hedging) | 离子阱 ≤16 比特 | "近乎翻倍"对冲有效性 | 研究 PoC | [A] |
| **摩根大通**(Pistoia 团队,2024) | 约束组合优化(分解管线) | 门模型 | 速度/精度提升(具体数未定) | 研究 | [B] |
| **高盛 + QC Ware + IonQ**(2021) | "浅"量子蒙特卡洛定价 | IonQ | 理论 ~100×(面向 5–10 年后硬件) | PoC | [A] |
| **高盛 + AWS**(~2023) | 组合优化(量子内点法 QIPM) | 资源估计 | 容错运行时估计达**"数百万年"** | 资源估计(清醒定调) | [B] |
| **法农 CIB + Pasqal + Multiverse**(2023) | 衍生品估值 + 交易对手降级预测 | 中性原子 ~50 比特 / 张量网络 | 6–15 月预测"与生产同精度" | 对标生产的 PoC | [A] |
| **CaixaBank/VidaCaixa + D-Wave**(2022) | 保险投资对冲 | D-Wave Leap 混合 | 计算时间从小时→分钟(**–90%**) | 试点,曾评估投产(最接近生产的退火案例) | [C] |
| **BBVA + Multiverse**(2021) | 组合优化(三法并行) | IBM-Q/D-Wave/张量网络 | 发现新优化方法 | 探索阶段(BBVA 自述) | [C] |
| **Mastercard + D-Wave**(2022) | 欺诈/忠诚度特征选择 | D-Wave 退火 | 100 客户样本 $151k vs $96k(厂商口径) | R&D 联盟 | [C] |
| **D-Wave 产品化**(2025-Q1) | 组合优化/预算分配 | 非线性混合求解器 | 支持至 200 万变量 | 商用能力(无具名银行生产案例) | [C] |
| **富国银行 + IBM**(2024) | 量子算法 + 抗量子安全 | IBM Quantum Network | ~10 篇同行评审论文 | 研究/探索 | [B/C] |
| **渣打 + IBM**(2026) | 量子探索 + 后量子密码 | — | — | 探索/安全 | [C] |
| **三菱日联 + PsiQuantum**(2024) | 光致变色分子模拟(材料,非金融!) | 容错路线 | — | 战略合作(**属材料科学,非资产配置**) | [B] |

**负面/澄清(避免误引):**
- **Ally Financial:** 未发现 2023–2026 量子活动。
- **Itaú:** 仅前述 QC Ware QML 论文;无其他量子-金融合作。
- **Bankia:** 已于 2021 并入 CaixaBank;勿作为独立 Multiverse 客户,改用 CaixaBank。
- **桥水(Bridgewater):** 本轮检索未发现公开的量子计算资产配置项目;勿臆造。

---

## 4. 技术瓶颈与"量子优势是否兑现"的批判性评估

撰写批判性论文时,以下四道"硬墙"+硬件现实最有力:

1. **容错资源天文数字。** [B] 高盛/AWS 的量子内点法组合优化端到端估计:即便 T 门以经典 GHz 速度运行,运行时"仍达数百万年";"渐近加速若交叉点(crossover)出现在大到无用的规模,则毫无价值"。
2. **去量子化(Dequantization)。** [A] Tang 及 Chia/Gilyén/Tang 等(arXiv:1910.06151):推荐系统、PCA、线性系统、SVM、SDP 的"指数级 QML 加速"对低秩问题可被经典采样算法以**多项式对数时间**复现——加速实为多项式级。Aaronson(*Read the Fine Print*,Nat. Phys. 2015):HHL 类指数加速依赖 QRAM、良态矩阵、且**不需读出完整解**——读出本身需 ~N 次测量,会摧毁指数加速。
3. **数据加载 / 态制备瓶颈。** [A/B] 从 N 个经典值制备任意量子态一般需 O(N)~O(2ⁿ) 操作,可在计算开始前就抵消优势;QRAM 仍"基本停留在理论"。金融的相关多资产/布朗路径分布加载是 NISQ 期权定价的主导成本。
4. **贫瘠高原 / 噪声诱导贫瘠高原。** [A] Wang, Cerezo et al.,*Noise-induced barren plateaus in VQAs*,Nat. Commun.(2021,arXiv:2007.14384):局域噪声下,若 ansatz 深度线性增长,梯度随比特数**指数消失**,且**无法靠初始化修复**——直接打击金融最依赖的 NISQ 变分路线(QAOA/VQE)。

**硬件现实与路线图:**
- **[A] Google Willow(2024-12):** 105 比特演示**低于阈值**纠错,逻辑错误率每增码距 2 抑制 ~2.14×,距离-7 码达 0.143%/周期——但这是**存储器里程碑,非应用优势**,且远未达金融规模逻辑比特。
- **[C/B] IBM 路线图:** Starling(2029)目标 ~200 逻辑比特 / 1 亿门(qLDPC 码),中间节点 Loon(2025)/Kookaburra(2026)/Cockatoo(2027);更远 Blue Jay 目标 2000 逻辑比特 / 10 亿门。**厂商目标,内在乐观、未经证实。**
- **[B/C] 分析机构判断:** McKinsey 认为容错约 2030(部分更早),但"许多专家预测 2035",路线图可信度存疑;金融经济价值 $4000–6000 亿是"到 2035 年"的长期预测,非当下价值。
- **[A/C] 行业自承:** "尚未在任何一家银行见到全面运行的量子金融系统";2025 的演示"仍是受控概念验证,而非运行中的量子金融系统"。

**对 HSBC/IBM 的批判性拆解(论文可重点用):** 它是 2025 年最强案例,但 (a) 范围窄(债券成交概率预测,非组合优化);(b) 混合架构;(c) **"优势"在经典模拟器上无法复现,疑为硬件噪声充当了有用的统计结构**——这意味着它可能是噪声伪影而非可泛化的量子计算优势;(d) 未被独立复现。引用其"34%"的同时务必并列这些保留。

---

## 5. 对论文的启示与研究空白(Research Gaps)

1. **"大类资产配置"(strategic / multi-asset allocation)本身的量子研究极少。** 绝大多数文献停留在**单一资产类别内的股票组合优化**;跨股/债/商品/另类的战略配置、宏观情景驱动的资产轮动几乎是空白——这是论文可主张的明确缺口。
2. **宏观经济量子建模薄弱。** 真正的宏观(GDP、通胀、利率、政策情景)QML 工作稀少且多为量子启发(Alaminos 等),缺乏与央行/宏观计量模型(DSGE、VAR)的严肃对比。
3. **基准不公平是普遍病。** 大量"优势"声明对标自选弱基线或参数匹配(非算力匹配)的经典模型;论文应呼吁标准化、算力匹配、含交易成本与样本外的基准(Fraunhofer 基准是范本)。
4. **量子启发式 vs 量子硬件的边界需厘清。** 当下金融真实收益多来自量子启发的经典方法;论文须明确:这**不是**量子优势,反而是去量子化的体现。
5. **风险方向更"诚实"但更远。** QAE 的二次加速可证明,却受制于容错;论文可对比"组合优化(近期可演示但无优势)"与"风险/定价(数学扎实但需 2030+ 硬件)"两条路径的不同时间尺度。

---

## 6. 中英术语对照表(Glossary)

| English | 中文 |
|---|---|
| Quantum advantage / supremacy | 量子优势 / 量子霸权 |
| NISQ (Noisy Intermediate-Scale Quantum) | 含噪中等规模量子 |
| Fault-tolerant quantum computing (FTQC) | 容错量子计算 |
| Logical / physical qubit | 逻辑 / 物理量子比特 |
| Quantum error correction (QEC) | 量子纠错 |
| Surface code / qLDPC code | 表面码 / 量子低密度奇偶校验码 |
| Below-threshold error correction | 低于阈值纠错 |
| T-gate / T-depth | T 门 / T 深度 |
| Logical clock speed | 逻辑时钟频率 |
| Decoherence | 退相干 |
| QAOA (Quantum Approximate Optimization Algorithm) | 量子近似优化算法 |
| VQE (Variational Quantum Eigensolver) | 变分量子本征求解器 |
| Variational quantum algorithm (VQA) | 变分量子算法 |
| Quantum annealing | 量子退火 |
| QUBO (Quadratic Unconstrained Binary Optimization) | 二次无约束二元优化 |
| Ising model / Hamiltonian | 伊辛模型 / 哈密顿量 |
| Ansatz | 拟设 / 试探波函数 |
| Barren plateau | 贫瘠高原(梯度消失) |
| XY-mixer / Dicke state | XY 混合器 / 迪克态 |
| Counterdiabatic optimization | 反绝热优化 |
| Quantum amplitude estimation (QAE) | 量子振幅估计 |
| Quantum Monte Carlo (integration) | 量子蒙特卡洛(积分) |
| Quadratic / exponential speedup | 二次 / 指数级加速 |
| Quantum Signal Processing (QSP) / QSVT | 量子信号处理 / 量子奇异值变换 |
| State preparation / data loading | 态制备 / 数据加载 |
| Amplitude encoding | 振幅编码 |
| QRAM (Quantum Random Access Memory) | 量子随机存取存储器 |
| Dequantization | 去量子化 |
| Quantum-inspired (classical) algorithm | 量子启发(经典)算法 |
| Tensor network | 张量网络 |
| Quantum machine learning (QML) | 量子机器学习 |
| Quantum neural network (QNN) | 量子神经网络 |
| Quantum kernel method | 量子核方法 |
| Exponential concentration | 指数集中 |
| Quantum reservoir computing (QRC) | 量子储备池计算 |
| Quantum GAN (qGAN) / QWGAN-GP | 量子生成对抗网络 |
| Crossover point | 交叉点 / 临界规模 |
| Portfolio optimization | 投资组合优化 |
| Asset allocation (strategic / multi-asset) | (战略 / 大类)资产配置 |
| Mean-variance (Markowitz) model | 均值-方差(马科维茨)模型 |
| Cardinality / budget constraint | 基数 / 预算约束 |
| Sharpe ratio | 夏普比率 |
| Value at Risk (VaR) | 风险价值 |
| Conditional VaR (CVaR) / Expected Shortfall | 条件风险价值 / 预期损失 |
| Economic Capital Requirement (ECR) | 经济资本要求 |
| Credit risk | 信用风险 |
| Deep hedging | 深度对冲 |
| Derivative / option pricing | 衍生品 / 期权定价 |
| Mixed-integer programming (MIP) | 混合整数规划 |
| Simulated annealing / Tabu search | 模拟退火 / 禁忌搜索 |
| Hierarchical Risk Parity (HRP) | 层次风险平价 |
| Trapped-ion / neutral-atom | 离子阱 / 中性原子 |
| Stylized facts | 典型化事实 |
| Regime detection / shift | 状态识别 / 状态切换 |
| Scenario generation | 情景生成 |
| Post-quantum cryptography / quantum-safe | 后量子密码学 / 抗量子安全 |

机构译名:摩根大通(JPMorgan Chase)、高盛(Goldman Sachs)、汇丰(HSBC)、西班牙对外银行(BBVA)、法国农业信贷银行企业与投资银行(Crédit Agricole CIB)、凯克萨银行(CaixaBank)/凯克萨人寿(VidaCaixa)、渣打银行(Standard Chartered)、富国银行(Wells Fargo)、三菱日联金融集团(MUFG)、伊塔乌联合银行(Itaú Unibanco)、万事达卡(Mastercard);厂商:IBM、IonQ、D-Wave、Pasqal、Multiverse Computing、QC Ware、PsiQuantum、Fujitsu。

---

## 7. 参考文献(按可信度分级)

### A 级——同行评审 / 权威综述(可直接引用)

1. Herman, Googin, Liu, ... Safro, *Quantum computing for finance*, **Nature Reviews Physics** 5, 450–465 (2023). arXiv:2307.11230. https://www.nature.com/articles/s42254-023-00603-1
2. Stopfer & Wagner (Fraunhofer IIS), *Quantum Portfolio Optimization: An Extensive Benchmark*, **arXiv:2509.17876** (2025). https://arxiv.org/abs/2509.17876
3. Mugel, Orús et al., *Dynamic Portfolio Optimization with Real Datasets*, **Phys. Rev. Research** 4, 013006 (2022). arXiv:2007.00017.
4. Stamatopoulos, Egger, Sun, Zoufal, Iten, Shen, Woerner, *Option Pricing using Quantum Computers*, **Quantum** 4, 291 (2020). https://quantum-journal.org/papers/q-2020-07-06-291/
5. Woerner & Egger, *Quantum Risk Analysis*, **npj Quantum Information** (2019). arXiv:1806.06893.
6. Egger, Gutiérrez, Mestre, Woerner, *Credit Risk Analysis using Quantum Computers*, **IEEE Trans. Computers** (2020). arXiv:1907.03044.
7. Chakrabarti, Krishnakumar, Mazzola, Stamatopoulos, Woerner, Zeng (Goldman/IBM), *A Threshold for Quantum Advantage in Derivative Pricing*, **Quantum** 5, 463 (2021). arXiv:2012.03819.
8. Stamatopoulos & Zeng (Goldman), *Derivative Pricing using Quantum Signal Processing*, **Quantum** 8, 1322 (2024). arXiv:2307.14310.
9. Stamatopoulos, Clader, Woerner, Zeng, *Quantum Risk Analysis of Financial Derivatives*, arXiv:2404.10088 (2024).
10. Babbush, McClean, Newman, Gidney, Boixo, Neven (Google), *Focus beyond quadratic speedups for error-corrected quantum advantage*, **PRX Quantum** 2, 010103 (2021). arXiv:2011.04149.
11. Thanasilp, Wang, Cerezo, Holmes, *Exponential concentration in quantum kernel methods*, **Nature Communications** 15 (2024). arXiv:2208.11060.
12. Wang, Fontana, Cerezo et al., *Noise-induced barren plateaus in variational quantum algorithms*, **Nature Communications** 12:6961 (2021). arXiv:2007.14384.
13. Cherrat, Kerenidis et al. (Itaú/QC Ware), *Improved financial forecasting via quantum machine learning*, **Quantum Machine Intelligence** 6(1) (2024). arXiv:2306.12965.
14. Leiden group, *Quantum generative modeling for financial time series with temporal correlations*, **Mach. Learn.: Sci. Technol.** (2025). arXiv:2507.22035.
15. Tang; Chia, Gilyén, Li, Lin, Tang, Wang, *Sampling-based sublinear low-rank matrix arithmetic / dequantization*, STOC 2019 / arXiv:1910.06151.
16. Aaronson, *Quantum Machine Learning Algorithms: Read the Fine Print*, **Nature Physics** (2015).
17. Google Quantum AI, *Quantum error correction below the surface code threshold*, **Nature** 638 (2024). doi:10.1038/s41586-024-08449-y.
18. Li, Mukhopadhyay, Bayat, Habibnia, *Quantum Reservoir Computing for Realized Volatility Forecasting*, **Phys. Rev. Research** (2025). arXiv:2505.13933.
19. Alaminos et al., *Quantum Computing and Deep Learning Methods for GDP Growth Forecasting*, **Computational Economics** 59(2) (2022).

### B 级——预印本 / 资源估计(标注为预印本)

20. Morapakula et al. (Qkrishi), *End-to-end hybrid quantum annealing portfolio pipeline*, arXiv:2504.08843 / Adv. Quantum Tech. (2025).
21. Egger et al. / Goldman–AWS, *端到端组合优化资源评估(量子内点法)*, AWS Quantum Technologies Blog (~2023).
22. *Quantum Monte Carlo simulations for financial risk analytics: scenario generation*, **Quantum** (2024). arXiv:2303.09682.
23. 多类 VQE(Dicke 态),arXiv:2508.13954 (2025)。
24. **[!]** 以下为 2025Q4–2026 预印本,引用前请核对 arXiv 编号与数字:VQE/IBEX-35(arXiv:2512.22001)、约束 QAOA-XY(arXiv:2602.14827)、QAOA 再平衡(arXiv:2603.16904)、离子阱大规模组合(arXiv:2602.23976)、Fujitsu PCE(arXiv:2511.21305)、QML 基准(arXiv:2601.03802)、QTCNN(arXiv:2512.06630)、几何/状态检测(arXiv:2605.17117 / 2511.21515)。

### C 级——机构新闻稿 / 行业媒体(仅作产业动态)

25. HSBC, *HSBC demonstrates world's first-known quantum-enabled algorithmic trading with IBM* (2025-09-25). https://www.hsbc.com/news-and-views/news/media-releases/2025/hsbc-demonstrates-worlds-first-known-quantum-enabled-algorithmic-trading-with-ibm ; IBM Quantum Blog: https://www.ibm.com/quantum/blog/hsbc-algorithmic-bond-trading
26. 摩根大通深度对冲:Risk.net (2023);JPMorganChase Technology Blog;arXiv:2303.16585。
27. 高盛+QC Ware+IonQ 概念验证:IonQ IR / BusinessWire (2021-09-21)。
28. 法农 CIB + Pasqal + Multiverse:CA-CIB 新闻室 / HPCwire (2023-01-26)。
29. CaixaBank/VidaCaixa + D-Wave:D-Wave / BusinessWire (2022-03-03)。
30. BBVA + Multiverse:BBVA 新闻室 / Finextra (2021)。
31. Mastercard + D-Wave:D-Wave / Mastercard 新闻室 (2022-07)。
32. D-Wave Q1 2025 结果(非线性混合求解器):BusinessWire (2025-05-08)。
33. McKinsey, *The Year of Quantum / Quantum technology use cases in finance* (2025/2026);Moody's, *Quantum computing in the financial sector: 2024 trends*。
34. IBM Quantum 路线图(Starling 2029 等):IBM Quantum Blog / The Quantum Insider (2025-06)。

> **慎引来源:** Quantum Zeitgeist、低门槛期刊(IJSAT)、部分 MDPI 文章——仅作"行业关注度"佐证,其性能/采用率数字未经证实。
