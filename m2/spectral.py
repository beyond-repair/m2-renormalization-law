"""G_n -> L_n -> spectrum -> LDOS_n pipeline.

Graph Green function on the exact recursive Sierpinski gasket.
This is a spectral observable pipeline. It is NOT a thrust prediction.

LDOS definitions (must be named before use):

- global_LDOS: (1/N) sum_k delta(lambda-lambda_k)
- local_LDOS(i): sum_k |psi_k(i)|^2 delta(lambda-lambda_k)
- corner_LDOS: average over the 3 degree-2 corners
- boundary_LDOS: alias of corner_LDOS on this graph
- interior_LDOS: average over degree-4 vertices

None of these is designated the force.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np

Edge = Tuple[int, int]


def _key(p: np.ndarray, nd: int = 10) -> Tuple[float, float]:
    return (round(float(p[0]), nd), round(float(p[1]), nd))


def build_gasket(level: int):
    c0 = np.array([0.0, 0.0])
    c1 = np.array([1.0, 0.0])
    c2 = np.array([0.5, math.sqrt(3.0) / 2.0])
    pos_map = {}
    positions = []
    edges = set()

    def vid(p):
        k = _key(p)
        if k not in pos_map:
            pos_map[k] = len(positions)
            positions.append(p.copy())
        return pos_map[k]

    def rec(a, b, c, d):
        if d == 0:
            ia, ib, ic = vid(a), vid(b), vid(c)
            for i, j in ((ia, ib), (ib, ic), (ic, ia)):
                if i != j:
                    edges.add((min(i, j), max(i, j)))
            return
        rec(a, 0.5 * (a + b), 0.5 * (c + a), d - 1)
        rec(0.5 * (a + b), b, 0.5 * (b + c), d - 1)
        rec(0.5 * (c + a), 0.5 * (b + c), c, d - 1)

    rec(c0, c1, c2, level)
    P = np.vstack(positions)
    corners = np.array([pos_map[_key(c0)], pos_map[_key(c1)], pos_map[_key(c2)]], dtype=int)
    return P, sorted(edges), corners


def laplacian_from_edges(n: int, edges: List[Edge]) -> np.ndarray:
    L = np.zeros((n, n), dtype=float)
    for i, j in edges:
        L[i, i] += 1.0
        L[j, j] += 1.0
        L[i, j] -= 1.0
        L[j, i] -= 1.0
    return L


@dataclass
class Spectrum:
    level: int
    evals: np.ndarray
    evecs: np.ndarray
    corners: np.ndarray
    degrees: np.ndarray


def spectrum(level: int) -> Spectrum:
    P, E, C = build_gasket(level)
    L = laplacian_from_edges(len(P), E)
    w, V = np.linalg.eigh(L)
    return Spectrum(level, w, V, C, np.diag(L))


def ldos_matrix(spec: Spectrum) -> np.ndarray:
    return spec.evecs ** 2


def partitioned_ldos_weights(spec: Spectrum) -> Dict[str, np.ndarray]:
    W = ldos_matrix(spec)
    corner_mask = np.zeros(W.shape[0], dtype=bool)
    corner_mask[spec.corners] = True
    interior_mask = spec.degrees >= 4.0 - 1e-12
    return {
        "global": W.mean(axis=0),
        "local_mean": W.mean(axis=0),
        "corner": W[corner_mask].mean(axis=0) if corner_mask.any() else W.mean(axis=0),
        "boundary": W[corner_mask].mean(axis=0) if corner_mask.any() else W.mean(axis=0),
        "interior": W[interior_mask].mean(axis=0) if interior_mask.any() else W.mean(axis=0),
    }


def raw_zeta(spec: Spectrum, s: float) -> float:
    w = spec.evals[spec.evals > 1e-10]
    return float(np.sum(w ** (-s)))


def green_at_shift(spec: Spectrum, z: complex) -> np.ndarray:
    w = spec.evals.astype(complex)
    return (spec.evecs * (1.0 / (z - w))) @ spec.evecs.T
