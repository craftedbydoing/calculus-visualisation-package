import plotly.graph_objects as go


def taylor_plotly(x, f_vals, taylor_vals, n, ylim=None):
    fig = go.Figure()

    fig.add_scatter(x=x, y=f_vals, mode="lines", name=r"$f(x)$")
    fig.add_scatter(x=x, y=taylor_vals, mode="lines",
                    name=r"$T_n(x)$",
                    line={"dash": "dash", "width": 2})

    if ylim:
        fig.update_yaxes(range=list(ylim))

    return fig
