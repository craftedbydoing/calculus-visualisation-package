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
