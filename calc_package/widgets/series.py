import matplotlib.pyplot as plt
import numpy as np
import math as m
from ipywidgets import IntSlider, interact, FloatSlider

from calc_package.core.functions import sample_clean
from calc_package.plotting.functions import plot_function
from calc_package.core.series import taylor_values


def taylor_explorer():
    functions = {
        "e^x": {"f": lambda x: np.exp(x),
                "deriv": lambda k, a: np.exp(a) + k*0,
                "a": 0},
        "sin(x)": {"f": lambda x: np.sin(x),
                   "deriv": lambda k, a: np.sin(a + k*np.pi/2),
                   "a": 0},
        "1/(1-x)": {"f": lambda x: 1/(1-x),
                    "deriv": lambda k, a: m.factorial(k) / (1-a)**(k+1),
                    "a": 0},
        "x^2": {"f": lambda x: x**2,
                "deriv": lambda k, a: (2*a if k == 0 else (2*a if k == 1 else (2 if k == 2 else 0))),
                "a": 0}
    }
    fig, ax = plt.subplots(figsize=(6, 5))

    def show(func_name, radius, n):
        entry = functions[func_name]
        f = entry["f"]
        deriv = entry["deriv"]
        a = entry["a"]
        domain = (a-radius, a+radius)

        x, y = sample_clean(f, domain)
        taylor_vals = taylor_values(x, a, deriv, n)

        y_min = np.nanmin(y)
        y_max = np.nanmax(y)
        pad = (y_max-y_min)*0.15

        ax.clear()
        plot_function(ax, x, y, label=func_name)
        plot_function(ax, x, taylor_vals, label="Taylor approx.")

        ax.legend()
        ax.set_ylim(y_min-pad, y_max+pad)
        fig.canvas.draw_idle()

    interact(
        show,
        func_name=list(functions.keys()),
        radius=FloatSlider(value=2, min=0.3, max=10, step=.1),
        n=IntSlider(value=0, min=0, max=20, step=1)
    )
