"""
D-Wave 量子退火:投资组合优化(QUBO / CQM)起步示例
====================================================

课题贴合度:这是与"大类资产配置 / 组合优化"最贴近的量子入口。
- 先在本地用「模拟退火」免费无限跑通;
- 注册 D-Wave Leap 后,把 token 填进去,一行切换到「真·5000+ 比特退火机」。

问题:从 N 个候选资产里选出恰好 K 个(基数约束),
      最大化「预期收益 - q × 组合方差」(马科维茨思想)。

依赖安装:
    pip install dwave-ocean-sdk
    # (dwave-ocean-sdk 已包含 dimod / dwave-system / dwave-samplers)
    # 可选,用真实行情:pip install yfinance

运行:
    python examples/dwave_portfolio_qubo.py            # 本地模拟退火(免费)
    USE_QPU=1 DWAVE_API_TOKEN=xxx python examples/dwave_portfolio_qubo.py   # 真机
"""

import os
import numpy as np
import dimod

# ----------------------------------------------------------------------
# 1. 数据:预期年化收益 mu 与协方差矩阵 sigma
#    这里用合成数据(结构与真实资产一致);想用真实行情见文末 load_real_data()
# ----------------------------------------------------------------------
def make_synthetic_data(n_assets=12, seed=42):
    rng = np.random.default_rng(seed)
    mu = rng.uniform(0.04, 0.18, size=n_assets)          # 年化预期收益 4%~18%
    A = rng.normal(0, 1, size=(n_assets, n_assets))
    cov = (A @ A.T) / n_assets                            # 半正定协方差
    vol = rng.uniform(0.10, 0.35, size=n_assets)         # 年化波动 10%~35%
    d = np.sqrt(np.diag(cov))
    cov = cov / np.outer(d, d) * np.outer(vol, vol)       # 缩放到目标波动
    return mu, cov


def build_bqm(mu, cov, K, q=0.5, penalty=None):
    """构造二元二次模型(BQM):x_i ∈ {0,1} 表示是否选资产 i。

    目标(最小化):  -mu·x  +  q · xᵀΣx   +  λ·(Σx_i - K)²
                    收益(取负)   风险      基数约束惩罚
    """
    n = len(mu)
    if penalty is None:
        # 惩罚系数要足够大,确保约束被满足;经验值取目标项量级的若干倍
        penalty = 5.0 * (np.abs(mu).max() + q * np.abs(cov).max())

    bqm = dimod.BinaryQuadraticModel(vartype="BINARY")

    # 线性项:-mu_i  +  惩罚展开的线性部分 λ(1 - 2K)
    for i in range(n):
        bqm.add_variable(i, -mu[i] + penalty * (1 - 2 * K))

    # 二次项:风险 q·Σ_ij  +  惩罚展开的交叉项 2λ
    for i in range(n):
        for j in range(i + 1, n):
            bqm.add_interaction(i, j, q * 2 * cov[i, j] + penalty * 2)
        # 对角风险项进入线性(因 x_i² = x_i)
        bqm.add_linear(i, q * cov[i, i])

    bqm.offset += penalty * K * K
    return bqm


def report(sample, mu, cov, q, label):
    chosen = [i for i, v in sample.items() if v == 1]
    w = np.zeros(len(mu));
    if chosen:
        w[chosen] = 1.0 / len(chosen)           # 等权重(选中后再做连续权重优化更佳)
    ret = float(w @ mu)
    risk = float(w @ cov @ w)
    print(f"\n[{label}]")
    print(f"  选中资产 (K={len(chosen)}): {chosen}")
    print(f"  组合预期收益: {ret:.4f}   组合方差: {risk:.4f}   "
          f"效用(ret - q·risk): {ret - q*risk:.4f}")


def main():
    K = 4            # 选 4 个资产
    q = 0.5          # 风险厌恶系数
    mu, cov = make_synthetic_data(n_assets=12)
    bqm = build_bqm(mu, cov, K=K, q=q)

    use_qpu = os.environ.get("USE_QPU") == "1"

    if not use_qpu:
        # ---------- 本地:模拟退火(免费、无限)----------
        from dwave.samplers import SimulatedAnnealingSampler
        sampler = SimulatedAnnealingSampler()
        res = sampler.sample(bqm, num_reads=200)
        report(res.first.sample, mu, cov, q, "本地 SimulatedAnnealing")

        # 小规模可顺便求"真正最优"做对照(经典基线!写论文必备)
        if bqm.num_variables <= 18:
            exact = dimod.ExactSolver().sample(bqm)
            report(exact.first.sample, mu, cov, q, "经典精确最优 ExactSolver(基线)")
    else:
        # ---------- 真机:D-Wave Advantage 量子退火 ----------
        # token 从 https://cloud.dwavesys.com/leap → Dashboard 复制
        from dwave.system import DWaveSampler, EmbeddingComposite
        token = os.environ["DWAVE_API_TOKEN"]
        sampler = EmbeddingComposite(DWaveSampler(token=token))
        res = sampler.sample(bqm, num_reads=1000, label="portfolio-qubo")
        report(res.first.sample, mu, cov, q, "D-Wave QPU(真·量子退火)")
        print("\n  本次 QPU 占用时间(微秒):",
              res.info.get("timing", {}).get("qpu_access_time"))


# ----------------------------------------------------------------------
# 可选:用真实行情替换合成数据
# ----------------------------------------------------------------------
def load_real_data(tickers, period="2y"):
    import yfinance as yf
    px = yf.download(tickers, period=period)["Close"].dropna()
    rets = px.pct_change().dropna()
    mu = rets.mean().values * 252                 # 年化收益
    cov = rets.cov().values * 252                 # 年化协方差
    return mu, cov
    # 用法:mu, cov = load_real_data(["AAPL","MSFT","GLD","TLT","XOM",...])


if __name__ == "__main__":
    main()
