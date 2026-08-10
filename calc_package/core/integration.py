import numpy as np


def riemann_sum(f: callable, a: float, b: float, n: int, method: str = "lower", samples_per_bin=50) -> tuple:
    """Computes riemann sum a returns needed values for plotting.

    Args:
        f (callable):
        a (float):
        b (float):
        n (int):
        method (str, optional): Defaults to "left".

    Returns:
        tuple[
            knots,
            height values of f at knots,
            width between knots,
            riemann sum
        ]
    """
    knots = np.linspace(a, b, n+1)
    width = (b-a)/n

    if method == "left":
        points = knots[:-1]
        heights = f(points)
    elif method == "right":
        points = knots[1:]
        heights = f(points)
    elif method == "midpoint":
        points = (knots[:-1] + knots[1:]) / 2
        heights = f(points)
    elif method == "lower" or method == "upper":
        left = knots[:-1]  # shape (n,)
        right = knots[1:]  # shape (n,)

        # shape (k,) — parametr
        t = np.linspace(0, 1, samples_per_bin)
        # broadcasting: (n,1) + (n,1)*(1,k) -> (n,k)
        points = left[:, None] + (right - left)[:, None] * t[None, :]

        vals = f(points)  # tvar (n,k)
        heights = vals.min(axis=1) if method == "lower" else vals.max(axis=1)
    else:
        raise ValueError(f"Unknown method: {method}")

    summation = np.sum(heights*width)

    return (knots, heights, width, summation)
