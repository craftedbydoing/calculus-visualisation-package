import numpy as np

def plot_function(ax, x, y):
    ax.plot(x, y)

    y_max = np.nanpercentile(y, 99.5)
    y_min = np.nanpercentile(y, 0.5)

    if (y_max - y_min) < 0.5:
        pad = 1
    else:
        pad = (y_max - y_min) * 0.1
    # ax.set_xlim(-10,10)
    ax.set_ylim(y_min - pad, y_max + pad)

def plot_epsilon_delta(ax, x, y, a, L, eps, delta, hole_x=None, ylim=None):
    plot_function(ax, x, y)
    ax.axhline(L, color="black")
    ax.axhline(L + eps, linestyle="--")
    ax.axhline(L - eps, linestyle="--")
    ax.axhspan(L - eps, L + eps, alpha=0.1)
    ax.axvline(a + delta, linestyle="--", color="green")
    ax.axvline(a - delta, linestyle="--", color="green")
    ax.axvspan(a - delta, a + delta, alpha=0.1)
    ax.plot(hole_x, L, 'o', markersize=7,
            markerfacecolor='white',
            markeredgecolor='black')