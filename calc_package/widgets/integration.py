import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import IntSlider, interact

from calc_package.core.functions import sample_clean
from calc_package.core.integration import riemann_sum
from calc_package.plotting.integration import plot_riemann


def riemann_visualisation():
    functions = {
        "e^x": {"f": lambda x: np.exp(x),
                "domain": (0, 3)},
    }

    fig, ax = plt.subplots()

    def show(func_name, n, method):
        entry = functions[func_name]
        f = entry["f"]
        a, b = entry["domain"]
        x, f_vals = sample_clean(f, (a, b))
        edges, heights, width, sumation = riemann_sum(f, a, b, n, method)

        ax.clear()
        plot_riemann(ax, x, f_vals, edges[:-1], heights, width)
        ax.set_title(f"Summation of $N={n}$ terms: {sumation:.04f}")
        fig.canvas.draw_idle()

    interact(
        show,
        func_name=list(functions.keys()),
        n=IntSlider(value=4, min=1, max=100, step=1),
        method=["left", "right", "midpoint"],
    )
