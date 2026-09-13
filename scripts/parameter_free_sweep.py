#!/usr/bin/env python3
"""Parameter-free M2 ratio lock.

No chi, eta, D_eff(n), or other n-dependent compensators.
Canonical W(n) = 0.08 * exp(0.23 * (n - 3)).
"""
from __future__ import annotations

import math

W0 = 0.08
XI = 0.23
ALPHA = 0.45
N3 = 3

EXPECTED = {
    "W_only": {2: 0.794533602503334, 3: 1.0, 4: 1.2586000099294778},
    "W_times_geom": {2: 0.5885434092617289, 3: 1.0, 4: 1.6991100134047954},
}
REJECTED_HYBRID = {2: 0.795, 3: 1.0, 4: 1.993}


def W(n: int) -> float:
    return W0 * math.exp(XI * (n - N3))


def geom(n: int) -> float:
    return (3.0 * ALPHA) ** n


def ratios(mode: str) -> dict[int, float]:
    raw = {}
    for n in (2, 3, 4):
        if mode == "W_only":
            raw[n] = W(n)
        elif mode == "W_times_geom":
            raw[n] = W(n) * geom(n)
        else:
            raise ValueError(mode)
    return {n: raw[n] / raw[3] for n in raw}


def main() -> None:
    print("M2 parameter-free sweep (Sweep-137)")
    print(f"W(n) = {W0} * exp({XI}*(n-{N3}))")
    print(f"alpha = {ALPHA}  (used only in W_times_geom)")
    print()
    for mode in ("W_only", "W_times_geom"):
        got = ratios(mode)
        print(f"=== {mode} ===")
        for n in (2, 3, 4):
            exp = EXPECTED[mode][n]
            ok = abs(got[n] - exp) < 1e-12
            print(f"  n={n}: {got[n]:.12f}  expected={exp:.12f}  {'OK' if ok else 'FAIL'}")
            if not ok:
                raise SystemExit(f"lock broken for {mode} n={n}")
        print()
    print("Rejected hybrid 0.795 : 1.000 : 1.993 is NOT produced by either model.")
    print("Do not introduce chi/eta/D_eff to force that hybrid.")


if __name__ == "__main__":
    main()
