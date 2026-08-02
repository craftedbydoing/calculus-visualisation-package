import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatRangeSlider, IntSlider
from calc_package.core.functions import sample_clean
from calc_package.plotting.functions import plot_function

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
