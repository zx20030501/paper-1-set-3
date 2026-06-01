"""
Qiskit QAOA(门模型):投资组合优化起步示例
==============================================

- 先在本地用 qiskit-aer 模拟器免费跑通 QAOA;
- 注册 IBM Quantum 后,把 token 填进去,切换到真·超导量子机(Heron r2)。

问题与 D-Wave 版一致:从 N 个资产里选 K 个,最大化「收益 - q·风险」。
这里用 qiskit-optimization 自动把问题编码成 Ising 哈密顿量并用 QAOA 求解。

依赖安装(注意:Qiskit API 演进较快,以下为 2025–2026 主流写法):
    pip install qiskit qiskit-aer qiskit-optimization qiskit-algorithms
    pip install qiskit-ibm-runtime    # 仅真机需要

运行:
    python examples/qiskit_qaoa_portfolio.py                 # 本地模拟器(免费)
    USE_QPU=1 IBM_QUANTUM_TOKEN=xxx python examples/qiskit_qaoa_portfolio.py   # 真机
"""

import os
import numpy as np
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_optimization.algorithms import MinimumEigenOptimizer


def make_synthetic_data(n_assets=6, seed=42):
    rng = np.random.default_rng(seed)
    mu = rng.uniform(0.04, 0.18, size=n_assets)
    A = rng.normal(0, 1, size=(n_assets, n_assets))
    cov = (A @ A.T) / n_assets
    vol = rng.uniform(0.10, 0.35, size=n_assets)
    d = np.sqrt(np.diag(cov))
    cov = cov / np.outer(d, d) * np.outer(vol, vol)
    return mu, cov


def build_problem(mu, cov, K, q=0.5):
    """构造带基数约束的二次 0/1 规划:max mu·x - q·xᵀΣx, s.t. Σx = K"""
    n = len(mu)
    qp = QuadraticProgram("portfolio")
    for i in range(n):
        qp.binary_var(name=f"x{i}")
    # 目标:最大化 收益 - 风险
    linear = {f"x{i}": mu[i] for i in range(n)}
    quadratic = {(f"x{i}", f"x{j}"): -q * cov[i, j]
                 for i in range(n) for j in range(n)}
    qp.maximize(linear=linear, quadratic=quadratic)
    # 基数约束 Σx_i = K(QuadraticProgramToQubo 会自动转成惩罚项)
    qp.linear_constraint(linear={f"x{i}": 1 for i in range(n)},
                         sense="==", rhs=K, name="budget")
    return qp


def get_sampler(use_qpu):
    if not use_qpu:
        # ---------- 本地:Aer 模拟器(免费)----------
        from qiskit_aer.primitives import SamplerV2
        return SamplerV2()
    else:
        # ---------- 真机:IBM Quantum ----------
        # token 从 https://quantum.cloud.ibm.com → 账户页复制
        from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
        service = QiskitRuntimeService(
            channel="ibm_quantum",
            token=os.environ["IBM_QUANTUM_TOKEN"],
        )
        backend = service.least_busy(operational=True, simulator=False)
        print(f"  使用真机后端: {backend.name}")
        return SamplerV2(mode=backend)


def report(x, mu, cov, q, label):
    chosen = [i for i, v in enumerate(x) if round(v) == 1]
    w = np.zeros(len(mu))
    if chosen:
        w[chosen] = 1.0 / len(chosen)
    ret = float(w @ mu); risk = float(w @ cov @ w)
    print(f"\n[{label}]")
    print(f"  选中资产 (K={len(chosen)}): {chosen}")
    print(f"  预期收益: {ret:.4f}   方差: {risk:.4f}   "
          f"效用: {ret - q*risk:.4f}")


def main():
    K, q = 3, 0.5
    mu, cov = make_synthetic_data(n_assets=6)   # 真机免费额度有限,先用小规模
    qp = build_problem(mu, cov, K=K, q=q)

    use_qpu = os.environ.get("USE_QPU") == "1"
    sampler = get_sampler(use_qpu)

    qaoa = QAOA(sampler=sampler, optimizer=COBYLA(maxiter=50), reps=2)
    solver = MinimumEigenOptimizer(qaoa)
    result = solver.solve(qp)
    report(result.x, mu, cov, q,
           "QAOA @ " + ("IBM QPU" if use_qpu else "本地模拟器"))

    # 经典基线对照(写论文必备):暴力枚举最优
    if len(mu) <= 16:
        from itertools import combinations
        best, best_u = None, -1e9
        for combo in combinations(range(len(mu)), K):
            w = np.zeros(len(mu)); w[list(combo)] = 1.0 / K
            u = w @ mu - q * (w @ cov @ w)
            if u > best_u:
                best_u, best = u, combo
        x = [1 if i in best else 0 for i in range(len(mu))]
        report(x, mu, cov, q, "经典枚举最优(基线)")


if __name__ == "__main__":
    main()
