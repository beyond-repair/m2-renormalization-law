# Spectrum pointer — not a force pipeline

**Date:** 2026-09-21  
**Claim level:** 1  
This file does **not** execute Stage 2 and does **not** produce \(F_n\).

`m2/spectral.py` uses the same combinatorial gasket Laplacian
\(L=D-A\) as [sierpinski-geometry-045 SPECTRUM.md](https://github.com/beyond-repair/sierpinski-geometry-045/blob/main/SPECTRUM.md).

Locked on that operator (free spectrum unless noted):

- \(\lambda_{\max}=6\) for \(n\ge 2\)
- \(\mathrm{Tr} L=6\cdot 3^n\)
- \(\mathrm{mult}(\lambda=6)=\frac{3}{2}(3^{n-1}-1)\) for \(n\ge 2\)
- Dirichlet \(\lambda_{\min}(L_n^D)/\lambda_{\min}(L_{n-1}^D)\to 1/5\)

These are graph facts. They may be used as regression locks for
`spectrum(level)` in this repo. They do **not**:

- select among Model A / Model B / hybrid M2 ratios,
- replace \(G_n\to\mathrm{LDOS}_n\to F_n\),
- identify corner_LDOS with thrust,
- import Kigami \(3/5\) or \(5/3\) into \(W(n)\).

Kigami factors live on harmonic extension / effective resistance
([KIGAMI_PCF.md](https://github.com/beyond-repair/sierpinski-geometry-045/blob/main/KIGAMI_PCF.md)).
Print-skew \(F\) is a different Poisson problem.

Stage 2 remains: geometry frozen, zero extra \(n\)-dependent knobs,
LDOS named before use. Fail ⇒ keep Model A or B only.
