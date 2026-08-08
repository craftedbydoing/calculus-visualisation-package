

def plot_riemann(ax, x, f_vals, edges, heights, width, ylim=None):

    ax.plot(x, f_vals)
    ax.bar(edges, heights, width=width, align="edge",
           alpha=0.4,
           edgecolor="black",
           linewidth=0.5)
