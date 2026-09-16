"""M2 renormalization law — frozen Stage-1 engineering weight."""

W0 = 0.08
XI = 0.23
N_PIN = 3
GHOST_BOUND = 0.125


def W(n: int | float) -> float:
    """Canonical Stage-1 law. Do not replace with exp(0.23*(n-1))."""
    import math
    return W0 * math.exp(XI * (n - N_PIN))
