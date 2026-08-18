import plotly.graph_objects as go


def plot_sequence(n, a, ylim=None):
    fig = go.Figure()

    fig.add_scatter(x=n, y=a, mode="markers", name="a_n",
                    marker={"size": 8, "opacity": 0.8,
                            "line": {"width": 1, "color": "darkblue"}})
    if ylim:
        fig.update_yaxes(range=list(ylim))

    return fig


def plot_convergence_plotly(n, a, L, eps, N, ylim=None):
    fig = go.Figure()

    fig.add_scatter(x=n, y=a, mode="markers", name="a_n",
                    marker={"size": 8, "opacity": 0.8,
                            "line": {"width": 1, "color": "darkblue"}},
                    hovertemplate="n = %{x}<br>a_n = %{y:.3f}<extra></extra>")
    fig.add_hrect(y0=L-eps, y1=L+eps, fillcolor="lightblue",
                  opacity=0.3, line_width=0)
    fig.add_hline(y=L, line_color="black")
    if N is not None:
        fig.add_vline(x=N, line_color="orange",
                      line_dash="dashdot", opacity=0.7)
    if ylim:
        fig.update_yaxes(range=list(ylim))

    return fig
