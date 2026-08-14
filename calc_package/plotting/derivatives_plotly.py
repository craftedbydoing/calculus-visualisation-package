import plotly.graph_objects as go


def plot_secant_to_tangent(x, f_vals, sec_vals, tan_vals, point_a, point_h, ylim=None):
    fig = go.Figure()

    fig.add_scatter(x=x, y=f_vals,   mode="lines", name="f(x)")
    fig.add_scatter(x=x, y=sec_vals, mode="lines", name="secant")
    fig.add_scatter(x=x, y=tan_vals, mode="lines", name="tangent",
                    line={"dash": "dash"})

    fig.add_scatter(x=[point_a[0], point_h[0]],
                    y=[point_a[1], point_h[1]],
                    mode="markers",
                    marker={"size": 10, "color": "magenta"},
                    showlegend=False)

    fig.update_xaxes(range=[x[0], x[-1]])
    if ylim is not None:
        fig.update_yaxes(range=list(ylim))

    return fig
