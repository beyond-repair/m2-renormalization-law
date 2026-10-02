<div align="center">

# M2 Renormalization Law

### How recursion depth **scales weight** — without rewriting galactic $W_\star$

[![RESEARCH](https://img.shields.io/badge/provisional-ansatz-f59e0b?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Sweep-137](https://img.shields.io/badge/ratios-parameter--free_lock-22c55e?style=for-the-badge)](FALSIFICATION.md)

</div>

---

## Why this exists

Fractal / recursive geometry needs a rule for “deeper mesh → stronger surface weight.”  
**M2** is that scaling ansatz. It is **provisional**, not a derived law of nature.

## Canonical form (Stage-1 freeze — residual-force / engineering)

$$
W(n) = 0.08\, e^{0.23(n-3)}
$$

- Pins $W(3)=0.08$
- Model-internal domain often quoted as $W(n)<0.125$ $\Rightarrow$ $n\le 4$ (**not** a proven physical no-ghost theorem)
- Option A: M2 multiplies engineering / LDOS / surface terms only. Galactic $W_\star=1/(4\pi)$ is not rescaled.

Deprecated indexing $W(n)=0.08\,e^{0.23(n-1)}$ — do not use for new residual-force work.

## Status of this tree

**RUNNABLE SKETCH — NOT A COMPLETE PRODUCT** (Claim-0).

The runnable check prints the Stage-1 weight, the two parameter-free ratio models, the combinatorial gasket spectrum, and one effective-action derivative. It does not derive \(W(3)=0.08\), \(\xi=0.23\), or a force \(F_n\). The rejected hybrid \(0.795:1:1.993\) stays rejected. No constant is refit to chase it.

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```

## Install, run, and test

No configuration file. The pins live in `m2/__init__.py` (`W0=0.08`, `XI=0.23`, `N_PIN=3`) and `m2/ratios.py` (`ALPHA=0.45`). Nothing is downloaded at runtime.

```bash
git clone https://github.com/beyond-repair/m2-renormalization-law.git
cd m2-renormalization-law
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
python3 scripts/parameter_free_sweep.py
m2-renormalization
python -m m2
pytest -q
```

`python -m m2` is the same report as `m2-renormalization`. The sweep script is stdlib-only and is the Sweep-137 ratio lock. The report also needs NumPy.

What a passing run reports, and does not claim:

| Command | What passes | What it does not say |
|---------|-------------|----------------------|
| `scripts/parameter_free_sweep.py` | Model A `0.794533602503 : 1 : 1.258600009929` and Model B `0.588543409262 : 1 : 1.699110013405` | That either triple is the rejected hybrid `0.795 : 1 : 1.993` |
| `m2-renormalization` | Same ratios; gasket locks for \(n\ge 2\): \(\lambda_{\max}=6\), \(\mathrm{Tr}\,L=6\cdot 3^n\), \(\mathrm{mult}(6)=\tfrac{3}{2}(3^{n-1}-1)\); finite-difference check of \(d\Gamma/dW\) | Stage 2 \(G_n\to\mathrm{LDOS}_n\to F_n\). \(\lambda_{\max}(n=1)\) is not 6. Raw \(\zeta(n=2,s=1/2)\) is not 0.35037322. \(W(5)\) is above 0.125 |
| `pytest -q` | The same locks, including the known misses | A physical measurement |

## Parameter-free ratios (Sweep-137 lock)

| Model | $F(2):F(3):F(4)$ | Status |
|-------|-------------------|--------|
| $W$-only (geometry frozen) | $0.795:1.000:1.259$ | consistent with $W(n)$ |
| $W\times(3\alpha)^n$, $\alpha=0.45$ | $0.589:1.000:1.699$ | consistent product model |
| Hybrid $0.795:1.000:1.993$ | — | **REJECTED** |

Adding $\chi$, $\eta$, $D_{\rm eff}(n)$, or efficiency factors to recover the hybrid is calibration, not prediction.

Ratio lock only (also listed above):

```bash
python3 scripts/parameter_free_sweep.py
```

Full lock text: [FALSIFICATION.md](FALSIFICATION.md)  
Graph-spectrum lock used by `m2/spectral.py` (not $F_n$): [SPECTRUM_POINTER.md](SPECTRUM_POINTER.md)

## Decisive next test

$$G_n \rightarrow \mathrm{LDOS}_n \rightarrow F_n$$

from the fixed 0.45 Sierpiński geometry with **no** fitted $n$-dependent parameters.  
If that chain does not recover a published ratio set, the set stays rejected.

## Status

README-level provisional ansatz.  
Freeze: [coherence-drive/docs/MATH_THEORY_CLOSURE.md](https://github.com/beyond-repair/coherence-drive/blob/main/docs/MATH_THEORY_CLOSURE.md)  
Portfolio map: [coherence-drive/docs/PORTFOLIO_MATH_2026-09-21.md](https://github.com/beyond-repair/coherence-drive/blob/main/docs/PORTFOLIO_MATH_2026-09-21.md)  
Ledger: [ware-constant-phenomenology](https://github.com/beyond-repair/ware-constant-phenomenology)  
Governance: [GOVERNANCE.md](GOVERNANCE.md) / [CLAIM_STATUS.md](CLAIM_STATUS.md)
