"""Effective action on the gasket Laplacian.

    K(W) = (omega + i eps)^2 I - W L
    Gamma(W) = -1/2 Tr ln K

Calculus identity (this implementation):

    dGamma/dW = +1/2 Tr(G L),   G = K^{-1}

The historically written formula F_W = -1/2 Tr(G L) therefore equals
-dGamma/dW, not dGamma/dW. Both are exposed. Neither is a spatial force F_q.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .spectral import spectrum


@dataclass
class ActionPoint:
    W: float
    omega: float
    eps: float
    Gamma: complex
    dGamma_dW: complex
    F_W_historical: complex  # -1/2 Tr(G L)  == -dGamma/dW


def evaluate(level: int, W: float, omega: float = 1.0, eps: float = 1e-8) -> ActionPoint:
    spec = spectrum(level)
    L = (spec.evecs * spec.evals) @ spec.evecs.T
    n = L.shape[0]
    z2 = (omega + 1j * eps) ** 2
    K = z2 * np.eye(n) - W * L
    ev = np.linalg.eigvals(K)
    Gamma = -0.5 * np.sum(np.log(ev))
    G = np.linalg.inv(K)
    half_tr = 0.5 * np.trace(G @ L)
    return ActionPoint(
        W=W,
        omega=omega,
        eps=eps,
        Gamma=complex(Gamma),
        dGamma_dW=complex(half_tr),
        F_W_historical=complex(-half_tr),
    )


def finite_difference_dGamma(level: int, W: float, h: float = 1e-6, **kw) -> complex:
    gp = evaluate(level, W + h, **kw).Gamma
    gm = evaluate(level, W - h, **kw).Gamma
    return (gp - gm) / (2.0 * h)
