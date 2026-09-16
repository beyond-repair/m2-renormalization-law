import numpy as np
from m2.effective_action import evaluate, finite_difference_dGamma
from m2.spectral import partitioned_ldos_weights, raw_zeta, spectrum


def test_spectrum_s2():
    spec = spectrum(2)
    assert spec.evals.shape[0] == 15
    assert spec.evals.min() < 1e-10
    assert abs(spec.evals.max() - 6.0) < 1e-8


def test_ldos_partitions_sum_to_one_per_mode():
    spec = spectrum(2)
    W = spec.evecs ** 2
    assert np.allclose(W.sum(axis=0), 1.0, atol=1e-10)
    parts = partitioned_ldos_weights(spec)
    assert set(parts) >= {"global", "corner", "interior", "boundary"}


def test_raw_zeta_not_the_quoted_regularized_value():
    z = raw_zeta(spectrum(2), 0.5)
    assert z > 1.0
    assert abs(z - 0.35037322) > 1.0


def test_effective_action_fd_matches_calculus():
    pt = evaluate(2, 0.08)
    fd = finite_difference_dGamma(2, 0.08)
    assert abs(fd - pt.dGamma_dW) / abs(pt.dGamma_dW) < 1e-6
    assert abs(pt.F_W_historical + pt.dGamma_dW) < 1e-10
