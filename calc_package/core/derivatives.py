import numpy as np


def calculate_slope(f, a, h):
    return (f(a+h)-f(a-h))/(2*h)
