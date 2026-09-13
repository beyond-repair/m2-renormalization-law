# Claim Status — m2-renormalization-law

**Classification:** RESEARCH  
**Claim level:** 1 (provisional scaling ansatz)  
**Governing source:** [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)  
**Canonical program:** [coherence-drive](https://github.com/beyond-repair/coherence-drive)  
**Lock date:** 2026-09-12 (Sweep-137 — ratio falsification lock)

## Supported claims

- Canonical Stage-1 form under Option A:
  $$W(n) = 0.08\, e^{0.23(n-3)}$$
  Pins $W(3)=0.08$. Does **not** rescale galactic $W_\star$.
- Shared exponent $\xi = 0.23$ is a **model parameter**, not a derived $\beta$-function.
- Parameter-free product model (fixed $\alpha=0.45$):
  $$F(n)\propto W(n)\,(3\alpha)^n$$
  yields relative ratios
  $$F(2):F(3):F(4)\approx 0.589:1.000:1.699$$
  Independent of whether $W(n)$ is indexed at $n-3$ or $n-1$ (the extra $e^{0.46}$ cancels in ratios).
- $W$-only ratios (geometry held fixed, no $(3\alpha)^n$):
  $$W(2):W(3):W(4)\approx 0.795:1.000:1.259$$

## Explicit non-claims

- Not derived from first principles.
- Not experimentally validated.
- Not a proven physical law, no-ghost theorem, or propulsion prediction.
- **Rejected as a parameter-free prediction:** $0.795:1.000:1.993$.
  That triple mixes the $W$-only $n=2$ ratio ($\approx 0.795$) with a stronger $n=4$ geometric boost and is **not** produced by any single published factor in this repo.
- Adding $\chi$, $\eta$, $D_{\rm eff}(n)$, efficiency factors, or other $n$-dependent compensators after observing the mismatch is **calibration**, not prediction.
- Deprecated indexing $W(n)=0.08\,e^{0.23(n-1)}$ must not be used for new residual-force work.
- No product, anomalous-thrust, energy-extraction, biological, PIF, or Orch-OR status.

## Decisive next test (Stage 2)

Derive, with geometry frozen at the 0.45 asymmetric Sierpiński tetrahedron and **zero** fitted $n$-dependent parameters:

$$G_n \rightarrow \mathrm{LDOS}_n \rightarrow F_n$$

If that chain reproduces a published ratio set, the set may be promoted.  
If not, the published set stays rejected.

## Evidence precedence

`scripts/parameter_free_sweep.py` is the numeric lock for the product-model ratios.  
Freeze text: [coherence-drive/docs/MATH_THEORY_CLOSURE.md](https://github.com/beyond-repair/coherence-drive/blob/main/docs/MATH_THEORY_CLOSURE.md)  
Audit addendum: [coherence-drive/docs/AUDIT_2026-09-12.md](https://github.com/beyond-repair/coherence-drive/blob/main/docs/AUDIT_2026-09-12.md)

Any elevation of claim level requires operator review + registry update in ADL-Governance.
