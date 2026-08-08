import numpy as np


def derivative_at_point(f, a, h=1e-3):
    return (f(a+h)-f(a-h))/(2*h)


def calculate_line_slope(f, a, h):
    return (f(a+h) - f(a))/(h)


def line_through_point(x, a, height_at_a, slope):
    return height_at_a + slope*(x-a)


def one_sided_slopes(f, a, h):
    right = (f(a + h) - f(a)) / h
    left = (f(a) - f(a - h)) / h
    return left, right


def derivative_exists(f, a, h=1e-3, tol=1e-6):
    left, right = one_sided_slopes(f, a, h)
    return np.isclose(left, right, atol=tol)
