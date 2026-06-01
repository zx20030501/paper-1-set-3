# 量子组合优化:起步示例与注册指南

两个可直接运行的最小示例,对应综述里的两条主线:
- `dwave_portfolio_qubo.py` — **量子退火**(D-Wave),与"组合优化/大类资产配置"最贴合,免费层就能跑真实规模。
- `qiskit_qaoa_portfolio.py` — **门模型 QAOA**(IBM Quantum),学 NISQ 算法与噪声。

两个脚本都**默认在本地免费模拟器上运行**,并附带**经典最优基线对照**(写论文必备)。装好依赖即可直接 `python` 跑,无需任何账号。需要真机时再注册、填 token、加一个环境变量切换。

## 1. 本地先跑(0 成本,无需注册)

```bash
pip install dwave-ocean-sdk
pip install qiskit qiskit-aer qiskit-optimization qiskit-algorithms

python examples/dwave_portfolio_qubo.py     # 模拟退火 + 精确最优基线
python examples/qiskit_qaoa_portfolio.py    # QAOA 模拟器 + 枚举最优基线
```

## 2. 注册真机账号(各 1 分钟,全程 "Continue with Google",无需设密码)

> 建议一律用 **Sign in with Google / Continue with Google**,选你的 Gmail 即可——
> 不用新建也不用记任何密码。若某服务强制设密码,请用你的密码管理器生成并保存,**不要让任何人(包括 AI)替你保管密码**。

### A. D-Wave Leap(量子退火)
1. 打开 https://cloud.dwavesys.com/leap/signup
2. 点 **"Sign up with Google"** → 选 `sdm7890@gmail.com` → 授权。
3. 进入后在 **Dashboard** 找到 **API Token**(`Solver API Token`),点复制。
4. 运行真机:
   ```bash
   USE_QPU=1 DWAVE_API_TOKEN=粘贴你的token python examples/dwave_portfolio_qubo.py
   ```
   免费层每月有秒级 QPU 额度,足够跑成百上千次本示例。

### B. IBM Quantum(门模型 QAOA)
1. 打开 https://quantum.cloud.ibm.com/
2. 点 **"Sign in / Create account"** → **Continue with Google** → 选 `sdm7890@gmail.com`。
3. 登录后在账户/仪表盘页复制 **API Token**(IBM Cloud API key)。
4. 运行真机:
   ```bash
   USE_QPU=1 IBM_QUANTUM_TOKEN=粘贴你的token python examples/qiskit_qaoa_portfolio.py
   ```
   Open Plan 免费层:每 28 天 10 分钟真机时间(用满 20 分钟可申请 180 分钟/年促销)。

## 3. 成本提示

- **本地模拟器 / 经典基线**:永远免费。
- **D-Wave 真机**:单次组合求解占用毫秒级 → 免费层够用,付费也是"以分计"。
- **IBM 真机**:免费层够学习;付费 Pay-as-you-go 是 $96/分钟,**只在最终出图时短跑几分钟**,别开长任务。
- 先把所有调参/优化循环放在模拟器,**真机只跑最终那一两次**,是省钱的关键。

## 4. 下一步(论文方向)

- 把 `make_synthetic_data()` 换成 `load_real_data([...])`(D-Wave 脚本文末有,用 `yfinance` 拉真实行情)。
- 扩大资产数 N,记录量子解 vs 经典最优的差距与耗时 → 这正是综述里"经典是否仍占优"的实证部分。
- D-Wave 进阶:改用 `LeapHybridCQMSampler` + `ConstrainedQuadraticModel` 原生处理约束,可上更大规模。
