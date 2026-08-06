import numpy as np


def derivative_at_point(f, a):
    h = 1e-3
    return (f(a+h)-f(a-h))/(2*h)


def calculate_slope_secant(f, a, h):
    return (f(a+h) - f(a))/(h)


def get_secant_values(f, x, a, sec_slope):
    return np.array(f(a) + sec_slope*(x-a))
