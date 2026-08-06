import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import FloatSlider, IntSlider, interact

from calc_package.core.sequences import find_N_for_limit, sample_sequence
from calc_package.plotting.sequences import plot_convergence


def sequence_convergence_explorer():
    EPS_MAX = 1.0
    sequences = {
        "1/n": {"f": lambda n: 1/n,
                "L": 0},
        "3-1/n": {"f": lambda n: 3-1/n,
                  "L": 3}
    }
    fig, ax = plt.subplots(figsize=(6, 6))

    def show(seq_name, eps, n_terms):
        entry = sequences[seq_name]
        L = entry["L"]
        n, a = sample_sequence(entry["f"], n_terms)
        N = find_N_for_limit(n, a, L, eps)

        a_max = np.max(a)
        a_min = np.min(a)
        y_max = np.max([a_max, L + EPS_MAX])
        y_min = np.min([a_min, L - EPS_MAX])

        if (y_max - y_min) < 0.5:
            pad = 1
        else:
            pad = (y_max - y_min) * 0.1
        ylim = (y_min - pad, y_max + pad)

        ax.clear()
        plot_convergence(ax, n, a, L, eps, N, ylim)
        fig.canvas.draw_idle()

    interact(
        show,
        seq_name=list(sequences.keys()),
        eps=FloatSlider(value=0.5, min=0.01, max=EPS_MAX, step=0.01),
        n_terms=IntSlider(value=10, min=1, max=70, step=1)
    )
