"""Parameter-free ratio models. No chi, eta, or D_eff(n).

Canonical weight is m2.W. Geometry factor is the fixed count (3*alpha)^n
with alpha=0.45. Neither model is a thrust prediction.
"""
from __future__ import annotations

from m2 import W

ALPHA = 0.45

# Printed by scripts/parameter_free_sweep.py. Do not edit either copy
# to force the rejected hybrid 0.795 : 1 : 1.993.
EXPECTED = {
    "W_only": {2: 0.794533602503334, 3: 1.0, 4: 1.2586000099294778},
    "W_times_geom": {2: 0.5885434092617289, 3: 1.0, 4: 1.6991100134047954},
}
REJECTED_HYBRID = {2: 0.795, 3: 1.0, 4: 1.993}


def geom(n: int) -> float:
    return (3.0 * ALPHA) ** n


def ratios(mode: str) -> dict[int, float]:
    raw: dict[int, float] = {}
    for n in (2, 3, 4):
        if mode == "W_only":
            raw[n] = W(n)
        elif mode == "W_times_geom":
            raw[n] = W(n) * geom(n)
        else:
            raise ValueError(mode)
    return {n: raw[n] / raw[3] for n in raw}


def ratios_match_lock(tol: float = 1e-12) -> bool:
    for mode, expected in EXPECTED.items():
        got = ratios(mode)
        for n, exp in expected.items():
            if abs(got[n] - exp) >= tol:
                return False
    return True
