from collections.abc import Callable

import numpy as np


def sample_sequence(
        f: Callable[[np.ndarray], np.ndarray],
        N: int = 20
) -> tuple[np.ndarray, np.ndarray]:
    """For a expression samples n and a_n (raw) values for a sequecne.

    Returns:
        tuple: n, a_n

        n: always [1, 2, ..., N]
        a_n: array [f(1), f(2), ..., f(N)]
    """
    n = np.arange(1, N+1)
    a_n = f(n)
    return n, a_n


def find_N_for_limit(n: np.ndarray, a: np.ndarray, L: float, eps: float) -> int:
    """For a given sequence's limit and epsilon computes N

    Args:
        n (np.ndarray): seq indexes
        a (np.ndarray): sequence values
        L (float): limit value
        eps (float): epsilon value

    Returns:
        int: index from which onwards sequence stays in epsilon band

    """
    if L in ["inf", "-inf", "DNE"]:
        return None

    inside_mask = np.abs(a - L) < eps
    outside_idx = np.where(~inside_mask)[0]  # indexes outside, output (smth, )

    if len(outside_idx) == 0:
        return n[0]  # all elements inside band
    if len(outside_idx) == len(a):  # no evidence sequence converges yet
        return None

    last_out = outside_idx[-1]
    return n[last_out+1]
