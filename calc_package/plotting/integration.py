

def plot_riemann(ax, x, f_vals, edges, heights, width, ylim=None):

    ax.plot(x, f_vals)
    ax.bar(edges, heights, width=width, align="edge",
           alpha=0.4,
           edgecolor="black",
           linewidth=0.5)


def plot_riemann_sandwich(ax, x, f_vals, edges, lower_heights, upper_heights, width, ylim=None):
    ax.plot(x, f_vals)
    ax.bar(edges, lower_heights, width=width, align="edge",
           alpha=0.5, color="steelblue", label="lower sum")

    ax.bar(edges, upper_heights - lower_heights,
           width=width, align="edge",
           bottom=lower_heights,
           alpha=0.5, color="salmon", label="gap")
