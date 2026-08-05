import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatRangeSlider, IntSlider, FloatSlider
from calc_package.core.functions import sample_clean, find_delta_for_limit
from calc_package.plotting.functions import plot_function, plot_epsilon_delta

def function_explorer():
    functions = {
        "3" : lambda x: 3 + 0*x,
        "x^2" : lambda x: x**2,
        "1/x" : lambda x: 1/x,
        "tan(x)" : lambda x: np.tan(x),
        "1/(x-1)" : lambda x: 1/(x - 1),
    }
    fig, ax = plt.subplots(figsize=(6,6))

    def show(func_names, domain, num_points):
        ax.clear() # clears the fig
        x, y = sample_clean(functions[func_names],
                            domain=domain,
                            num_points=num_points)
        plot_function(ax, x, y)
        ax.set_title(f"f(x) = {func_names}")
        fig.canvas.draw_idle() # "redraw command"

    interact(
        show,
        func_names=list(functions.keys()),
        domain=FloatRangeSlider(value=(-5, 5), min=-20, max=20, step=0.5),
        num_points=IntSlider(value=500, min=3, max=1000, step=1)
    )

def epsilon_delta_explorer():
    EPS_MAX = 1
    functions = {
        "sin(x)/x" : {"f" : lambda x: np.sin(x)/x,
                      "a" : 0,
                      "L" : 1,
                      "hole_x" : 0},
        # "2/(3-x)" : {"f" : lambda x: 2/(3-x),
        #             "L" : 3}
    }
    fig, ax = plt.subplots(figsize=(6,6))

    def show(func_name, eps, radius):
        entry = functions[func_name]
        L = entry["L"]
        a = entry["a"]
        domain = (a - radius, a + radius)
        x, y = sample_clean(entry["f"], domain)
        delta = find_delta_for_limit(x, y, a, L, eps)
    
        ylim = (L - EPS_MAX*1.2, L + EPS_MAX*1.2)

        ax.clear()
        plot_epsilon_delta(ax, x, y, a, L, eps, delta, entry["hole_x"], ylim=ylim)
        fig.canvas.draw_idle()

    interact(
        show,
        func_name = list(functions.keys()),
        eps = FloatSlider(value=0.3, min=0.01, max=EPS_MAX, step=0.01),
        radius=FloatSlider(value=3, min=0.1, max=10, step=0.1),
    )
