import math
from m2 import GHOST_BOUND, W


def test_canonical_pins_and_bound():
    assert abs(W(3) - 0.08) < 1e-15
    assert abs(W(2) - 0.08 * math.exp(0.23 * (2 - 3))) < 1e-15
    assert abs(W(2) - 0.063563) < 5e-6
    assert abs(W(4) - 0.100688) < 5e-6
    assert W(2) < GHOST_BOUND
    assert W(3) < GHOST_BOUND
    assert W(4) < GHOST_BOUND
    assert W(5) > GHOST_BOUND


def test_rejected_index_is_not_canonical():
    rejected_W3 = 0.08 * math.exp(0.23 * (3 - 1))
    assert rejected_W3 > 0.12
    assert abs(W(3) - rejected_W3) > 0.04
