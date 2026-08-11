import numpy as np
import math

def taylor_values(x, a, deriv, n):
    """
    
    Args:

        x: array of x's where function live
        a: point of expansion
        deriv: callable deriv(k, a) -> k-th derivative of f at a
        n: degree of taylor

    Returns: 
        array values of T_n(x)
    """

    result = np.zeros_like(x, dtype=float)
    for k in range(n+1):
        result += (deriv(k, a)) * (1/math.factorial(k)) * ((x - a)**k)

    return result