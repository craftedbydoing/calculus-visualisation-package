import plotly.graph_objects as go


def plot_convergence_plotly(x, f_vals, taylor_vals, n, ylim=None):
    fig = go.Figure()

    fig.add_scatter(x=x, y=f_vals, mode="lines", name="f(x)")
    fig.add_scatter(x=x, y=taylor_vals, mode="lines",
                    name=f"Taylor stupně {n}",
                    line={"dash": "dash", "width": 2})

    if ylim:
        fig.update_yaxes(range=list(ylim))

    return fig
