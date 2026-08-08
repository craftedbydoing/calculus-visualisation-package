import numpy as np


def riemann_sum(f: callable, a: float, b: float, n: int, method: str = "left") -> tuple:
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

    if method == "left":
        points = knots[:-1]
    elif method == "right":
        points = knots[1:]
    elif method == "midpoint":
        points = (knots[:-1] + knots[1:]) / 2
    else:
        raise ValueError(f"Unknown method: {method}")

    width = (b-a)/n
    heights = f(points)
    summation = np.sum(heights*width)

    return (knots, heights, width, summation)
