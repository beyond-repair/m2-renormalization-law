# M2 Falsification Lock — Sweep-137

**Date:** 2026-09-12  
**Status:** RESEARCH / claim level 1  
**Rule:** no post-hoc $n$-dependent compensators.

## 1. What failed

A previously circulated target

$$F(2):F(3):F(4)\ \stackrel{?}{=}\ 0.795:1.000:1.993$$

is **not** a parameter-free consequence of

$$W(n)=0.08\,e^{0.23(n-3)},\qquad \alpha=0.45.$$

## 2. Two internally consistent models (no extra knobs)

### Model A — $W$ only (geometry frozen)

$$\frac{F(n)}{F(3)}=\frac{W(n)}{W(3)}=e^{0.23(n-3)}$$

| $n$ | ratio |
|-----|-------|
| 2 | $0.79453$ |
| 3 | $1.00000$ |
| 4 | $1.25860$ |

### Model B — $W$ times static geometric count $(3\alpha)^n$

$$F(n)\propto W(n)\,(3\alpha)^n$$

| $n$ | ratio |
|-----|-------|
| 2 | $0.58854$ |
| 3 | $1.00000$ |
| 4 | $1.69911$ |

Model B is the executed product-model result previously quoted as $\approx 0.589:1:1.699$.

The $n-3$ vs $n-1$ indexing of $W$ **cancels in ratios**. Indexing is not the source of the $1.993$ discrepancy.

## 3. Why $0.795:1:1.993$ is rejected

That triple is a **hybrid**:

- $n=2$ matches Model A ($W$-only),
- $n=4$ exceeds both Model A ($1.259$) and Model B ($1.699$).

No single factor published in this repository produces both ends at once.  
Reaching $1.993$ requires an extra $n$-dependent amplifier (examples previously proposed: $D_{\rm eff}(n)$, $\chi$, $\eta$, $\cos$-modulation, pinch-efficiency). Those are compensators.

## 4. Forbidden moves

- Fit $\chi,\eta,D_{\rm eff},\kappa$ to recover $0.795:1:1.993$.
- Treat ADCE photon momentum as anomalous vacuum propulsion.
- Promote biological / PIF / Orch-OR coupling as part of M2.
- Use the design target $3\times 10^{-8}\,\mathrm{N/W}$ to define any coupling.

## 5. Allowed next derivation (only this elevates the claim)

Fixed hardware: asymmetric 0.45 Sierpiński tetrahedron ([sierpinski-geometry-045](https://github.com/beyond-repair/sierpinski-geometry-045)).

$$G_n(\mathbf{r},\mathbf{r},\omega)\ \to\ \rho_n(\mathbf{r},\omega)\ \to\ T^{\rm info}_n\ \to\ F_n$$

with

$$\rho(\mathbf{r},\omega)=\frac{2\omega}{\pi c^2}\operatorname{Im} G(\mathbf{r},\mathbf{r},\omega).$$

Pass: ratios emerge from the spectrum of that geometry.  
Fail: keep Model A or Model B as the only honest published ratios; drop $0.795:1:1.993$.

## 6. Reproduction

```bash
python3 scripts/parameter_free_sweep.py
```

Expected stdout lock is encoded in the script (`EXPECTED` dict). Changing `EXPECTED` without changing the formula is a claim-level violation.
