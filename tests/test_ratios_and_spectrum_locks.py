"""Locks already stated in FALSIFICATION.md and SPECTRUM_POINTER.md.

These tests fail if a constant is edited to chase the rejected hybrid
or the quoted regularized zeta. They do not assert a force ratio.
"""
import importlib.util
from pathlib import Path

import pytest

from m2.ratios import EXPECTED, REJECTED_HYBRID, ratios, ratios_match_lock
from m2.report import QUOTED_REGULARIZED_ZETA, action_point, spectrum_locks_hold, spectrum_rows
from m2.spectral import raw_zeta, spectrum


def _load_sweep():
    path = Path(__file__).resolve().parents[1] / "scripts" / "parameter_free_sweep.py"
    spec = importlib.util.spec_from_file_location("parameter_free_sweep", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_package_ratios_match_sweep_script_lock():
    sweep = _load_sweep()
    assert ratios_match_lock()
    for mode in ("W_only", "W_times_geom"):
        got = ratios(mode)
        assert sweep.ratios(mode) == pytest.approx(got)
        for n in (2, 3, 4):
            assert got[n] == pytest.approx(sweep.EXPECTED[mode][n])
            assert EXPECTED[mode][n] == sweep.EXPECTED[mode][n]


def test_rejected_hybrid_is_not_either_model():
    for mode in ("W_only", "W_times_geom"):
        got = ratios(mode)
        assert abs(got[4] - REJECTED_HYBRID[4]) > 0.2


def test_spectrum_pointer_locks_and_known_misses():
    rows = spectrum_rows((0, 1, 2, 3))
    assert spectrum_locks_hold(rows)
    by_level = {row["level"]: row for row in rows}
    assert by_level[0]["lambda_max"] == pytest.approx(3.0)
    assert by_level[1]["lambda_max"] == pytest.approx(5.30277563773, rel=1e-9)
    assert abs(by_level[1]["lambda_max"] - 6.0) > 0.5
    z = raw_zeta(spectrum(2), 0.5)
    assert z == pytest.approx(by_level[2]["zeta_s_half"])
    assert abs(z - QUOTED_REGULARIZED_ZETA) > 1.0


def test_action_finite_difference_in_report():
    point = action_point()
    assert point["fd_rel"] < 1e-6
    assert abs(point["F_W_historical"] + point["dGamma_dW"]) < 1e-10
