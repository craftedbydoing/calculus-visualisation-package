import numpy as np
from collections.abc import Callable

def sample_raw(
        f: Callable[[np.ndarray], np.ndarray],
        domain: tuple[float, float],
        num_points: int = 500
        ) -> tuple[np.ndarray, np.ndarray]:
    """For a function on a given domain samples x and y (raw) values.
    
    Returns:
        x, y: arrays of sampled values both for x and y
    """
    a, b = domain
    x = np.linspace(a, b, num_points)
    y = f(x)
    return x, y

def mask_discontinuities(y: np.ndarray, factor: float = 50) -> np.ndarray:
    """Filters the y values around discontinuities and rewrites them to 

    Args:
        y (np.ndarray): y values
        factor (float, optional): how many times larger has to the "bad" value around discontinuity be to be filtered, defaults to 50

    Returns:
        np.ndarray: fresh new array with np.nan values around discontinuity
    """
    d = np.abs(np.diff(y))
    med = np.median(d)
    if med == 0: # constant function
        return y.copy()
    bad_values = d > med*factor

    y_clean = y.copy()
    y_clean[1:][bad_values] = np.nan

    return y_clean

def sample_clean(
        f: Callable[[np.ndarray], np.ndarray],
        domain: tuple[float, float],
        num_points: int = 500,
        factor: float = 50
        ) -> tuple[np.ndarray, np.ndarray]:
    """For a function on a given domain samples x and y (cleaned) values.
    
    Returns:
        x, y: arrays of sampled values both for x and y
    """
    x, y = sample_raw(f, domain, num_points)
    y = mask_discontinuities(y, factor)
    return x, y

def find_delta_for_limit(x: np.ndarray, y: np.ndarray, a: float, L: float, eps: float) -> float:
    """For a given function's limit, a value and epsilon computes sufficient delta

    Args:
        x (np.ndarray): sampled x's for our function
        y (np.ndarray): sampled y's for our function
        a (float): value we are approaching with x
        L (float): limit value
        eps (float): epsilon value

    Returns:
        delta: delta from eps-delta def of a limit

    """
    inside_mask = np.abs(y - L) < eps
    outside_idx = np.where(~inside_mask)[0] # indexes outside, output (smth, )

    if len(outside_idx) == 0:
        return 1 # all elements inside band -> set delta to be 1 as a default
    if len(outside_idx) == len(y): # doesnt make really sense
        return  0

    x_idxs_right_of_a = np.where(x > a)[0]
    x_idxs_left_of_a = np.where(x < a)[0]

    right_outside = np.intersect1d(x_idxs_right_of_a, outside_idx)
    if len(right_outside) == 0: # whole right side inside epsilon band
        delta_right = np.inf
    else:
        delta_right = abs(x[np.min(right_outside)] - a)

    left_outside = np.intersect1d(x_idxs_left_of_a, outside_idx)
    if len(left_outside) == 0: # whole left side inside epsilon band
        delta_left = np.inf
    else:
        delta_left = abs(x[np.max(left_outside)] - a)

    delta = min(delta_left, delta_right)

    return delta





