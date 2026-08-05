import numpy as np

def plot_function(ax, x, y):
    ax.plot(x, y)

def plot_epsilon_delta(ax, x, y, a, L, eps, delta, hole_x=None, ylim=None):

    plot_function(ax, x, y)
    ax.axhline(L, color="black")
    ax.axhline(L + eps, linestyle="--")
    ax.axhline(L - eps, linestyle="--")
    ax.axhspan(L - eps, L + eps, alpha=0.1)
    ax.axvline(a + delta, linestyle="--", color="green")
    ax.axvline(a - delta, linestyle="--", color="green")
    ax.axvspan(a - delta, a + delta, alpha=0.1)
    if hole_x is not None:
        ax.plot(hole_x, L, 'o', markersize=7,
                markerfacecolor='white',
                markeredgecolor='black')

    ax.set_title(rf"$\delta = {delta:.2f}$  (pro $\varepsilon$ = {eps:.2f})")
    if ylim:
        ax.set_ylim(ylim[0], ylim[1])