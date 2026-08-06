
def plot_sequence(ax, n, a):
    ax.scatter(n, a)


def plot_convergence(ax, n, a, L, eps, N, ylim: tuple | None = None):

    plot_sequence(ax, n, a)

    ax.axhspan(L - eps, L + eps, alpha=0.2)
    ax.axhline(L, color="black")
    ax.axhline(L+eps, linestyle="--")
    ax.axhline(L-eps, linestyle="--")

    if N is not None:
        ax.axvline(N, color="magenta", linestyle="-.", alpha=0.7)
        ax.set_title(rf"$a_n$,  $N = {N}$  (pro $\varepsilon$ = {eps:.2f})")
    else:
        ax.text(0.5, 0.5, "Zatím bez evidence konvergence",
                transform=ax.transAxes, ha="center", color="red")
        ax.set_title(
            rf"$a_n$,  $N$ zatím nenalezeno ($\varepsilon$ = {eps:.2f})")

    if ylim:
        ax.set_ylim(ylim[0], ylim[1])
