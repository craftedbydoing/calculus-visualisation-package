
from calc_package.plotting.functions import plot_function


def plot_secant_to_tangent(ax, x, f_vals, sec_vals, tan_vals, point_a, point_h, ylim=None):
    plot_function(ax, x, f_vals, label="$f(x)$")
    plot_function(ax, x, sec_vals, label="secant")
    plot_function(ax, x, tan_vals, label="tangent")

    ax.set_xlim(x[0], x[-1])
    if ylim is not None:
        ax.set_ylim(ylim[0], ylim[1])

    ax.scatter(point_a[0], point_a[1], c="magenta")
    ax.scatter(point_h[0], point_h[1], c="magenta")
