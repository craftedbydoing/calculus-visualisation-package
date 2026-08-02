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