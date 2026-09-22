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

## Parameter-free ratios (Sweep-137 lock)

| Model | $F(2):F(3):F(4)$ | Status |
|-------|-------------------|--------|
| $W$-only (geometry frozen) | $0.795:1.000:1.259$ | consistent with $W(n)$ |
| $W\times(3\alpha)^n$, $\alpha=0.45$ | $0.589:1.000:1.699$ | consistent product model |
| Hybrid $0.795:1.000:1.993$ | — | **REJECTED** |

Adding $\chi$, $\eta$, $D_{\rm eff}(n)$, or efficiency factors to recover the hybrid is calibration, not prediction.

Reproduce:

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
