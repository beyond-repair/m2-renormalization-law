"""Print the numbers this tree actually computes.

Does not fit xi, the 0.08 pin, or alpha. Does not run Stage 2
(G_n -> LDOS_n -> F_n). Exit 0 means the in-tree locks hold, not
that a force ratio was measured.
"""
from __future__ import annotations

import math

import numpy as np

from m2 import GHOST_BOUND, N_PIN, W, W0, XI
from m2.effective_action import evaluate, finite_difference_dGamma
from m2.ratios import ALPHA, EXPECTED, REJECTED_HYBRID, ratios, ratios_match_lock
from m2.spectral import build_gasket, laplacian_from_edges, raw_zeta, spectrum

QUOTED_REGULARIZED_ZETA = 0.35037322


def _vertex_formula(level: int) -> int:
    # SG iteration with level 0 = one triangle: (3^{n+1} + 3) / 2.
    return (3 ** (level + 1) + 3) // 2


def _trace_formula(level: int) -> float:
    return 6.0 * (3**level)


def _mult6_formula(level: int) -> float:
    return 1.5 * (3 ** (level - 1) - 1)


def spectrum_rows(levels: range | tuple[int, ...] = (0, 1, 2, 3)) -> list[dict]:
    rows = []
    for level in levels:
        spec = spectrum(level)
        _positions, edges, _corners = build_gasket(level)
        lap = laplacian_from_edges(spec.evals.shape[0], edges)
        mult6 = int(np.sum(np.abs(spec.evals - 6.0) < 1e-8))
        claimed = level >= 2
        rows.append(
            {
                "level": level,
                "N": int(spec.evals.shape[0]),
                "N_formula": _vertex_formula(level),
                "edges": len(edges),
                "TrL": float(np.trace(lap)),
                "TrL_formula": _trace_formula(level),
                "lambda_max": float(spec.evals.max()),
                "lambda_min": float(spec.evals.min()),
                "mult6": mult6,
                "mult6_formula": _mult6_formula(level) if claimed else None,
                "lambda_max_claimed_6": claimed,
                "zeta_s_half": raw_zeta(spec, 0.5),
            }
        )
    return rows


def spectrum_locks_hold(rows: list[dict] | None = None, tol: float = 1e-8) -> bool:
    rows = rows if rows is not None else spectrum_rows()
    for row in rows:
        if row["N"] != row["N_formula"]:
            return False
        if abs(row["TrL"] - row["TrL_formula"]) > tol:
            return False
        if row["lambda_max_claimed_6"]:
            if abs(row["lambda_max"] - 6.0) > tol:
                return False
            if row["mult6_formula"] is None or abs(row["mult6"] - row["mult6_formula"]) > tol:
                return False
        elif abs(row["lambda_max"] - 6.0) <= tol:
            # Pointer claims lambda_max=6 only for n>=2. Levels 0 and 1 must miss.
            return False
    return True


def action_point() -> dict:
    level = 2
    weight = W(N_PIN)
    point = evaluate(level, weight)
    fd = finite_difference_dGamma(level, weight)
    denom = abs(point.dGamma_dW)
    rel = abs(fd - point.dGamma_dW) / denom if denom else math.inf
    return {
        "level": level,
        "W": weight,
        "omega": point.omega,
        "eps": point.eps,
        "Gamma": point.Gamma,
        "dGamma_dW": point.dGamma_dW,
        "F_W_historical": point.F_W_historical,
        "fd_rel": rel,
    }


def main() -> None:
    print("M2 renormalization law — Claim-0 numeric report")
    print("Not a thrust measurement. Constants are not refit.")
    print(f"W(n) = {W0} * exp({XI}*(n-{N_PIN}))")
    print(f"ghost-style model cut W < {GHOST_BOUND} (not a no-ghost theorem)")
    print(f"alpha = {ALPHA} (Model B only)")
    print()
    print("=== W(n) ===")
    for n in range(1, 6):
        value = W(n)
        side = "below cut" if value < GHOST_BOUND else "ABOVE cut"
        print(f"  n={n}: W={value:.12f}  {side}")
    print("  miss: W(5) crosses 0.125. The cut is a model pin, not a derived bound.")
    print()
    print("=== parameter-free ratios F(2):F(3):F(4) ===")
    ok_ratios = ratios_match_lock()
    for mode in ("W_only", "W_times_geom"):
        got = ratios(mode)
        print(f"  {mode}")
        for n in (2, 3, 4):
            exp = EXPECTED[mode][n]
            flag = "OK" if abs(got[n] - exp) < 1e-12 else "FAIL"
            print(f"    n={n}: {got[n]:.12f}  lock={exp:.12f}  {flag}")
    hybrid = REJECTED_HYBRID
    print("  rejected hybrid (not produced): "
          f"{hybrid[2]:.3f} : {hybrid[3]:.3f} : {hybrid[4]:.3f}")
    a4 = ratios("W_only")[4]
    b4 = ratios("W_times_geom")[4]
    print(f"  miss vs hybrid at n=4: Model A {a4:.6f}, Model B {b4:.6f}, target {hybrid[4]:.3f}")
    print("  do not add chi, eta, or D_eff(n) to close that gap")
    print()
    print("=== gasket Laplacian (combinatorial L=D-A) ===")
    rows = spectrum_rows()
    for row in rows:
        claim = "claimed" if row["lambda_max_claimed_6"] else "NOT claimed (n<2)"
        mult = row["mult6_formula"]
        mult_s = f"{mult:.1f}" if mult is not None else "n/a"
        print(
            f"  n={row['level']}: N={row['N']} (formula {row['N_formula']})  "
            f"E={row['edges']}  TrL={row['TrL']:.1f} (formula {row['TrL_formula']:.1f})  "
            f"lambda_max={row['lambda_max']:.8f} [{claim}]  "
            f"mult(6)={row['mult6']} (formula {mult_s})  "
            f"zeta(s=1/2)={row['zeta_s_half']:.6f}"
        )
    z2 = next(row["zeta_s_half"] for row in rows if row["level"] == 2)
    print(
        f"  miss: raw zeta(level=2, s=1/2)={z2:.6f} "
        f"is not the quoted regularized value {QUOTED_REGULARIZED_ZETA}"
    )
    l1 = next(row["lambda_max"] for row in rows if row["level"] == 1)
    print(f"  miss: lambda_max(level=1)={l1:.8f} is not 6; the lock starts at n>=2")
    print("  these locks are graph facts. They do not select Model A, Model B, or F_n.")
    print()
    point = action_point()
    print("=== effective action at level=2, W=W(3), omega=1, eps=1e-8 ===")
    print(f"  Gamma = {point['Gamma'].real:.12f} {point['Gamma'].imag:+.6e}j")
    print(f"  dGamma/dW = {point['dGamma_dW'].real:.12f} {point['dGamma_dW'].imag:+.6e}j")
    print(f"  historical F_W = -dGamma/dW  (rel FD error {point['fd_rel']:.3e})")
    print("  miss: this derivative is not a spatial force and is not Stage 2 LDOS->F_n")
    print()
    print("experimental_validation = false")
    print("thrust_validated = false")
    print("energy_extraction_validated = false")
    ok_spec = spectrum_locks_hold(rows)
    ok_fd = point["fd_rel"] < 1e-6
    if not (ok_ratios and ok_spec and ok_fd):
        raise SystemExit("in-tree lock failed (ratios, spectrum identity, or finite difference)")


if __name__ == "__main__":
    main()
