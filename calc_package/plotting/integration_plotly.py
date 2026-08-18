import plotly.graph_objects as go


def plot_riemann(x, f_vals, edges, heights, width, ylim=None):

    fig = go.Figure()
    fig.add_scatter(x=x, y=f_vals, mode="lines", name="f(x)")
    fig.add_bar(x=edges[:-1], y=heights, width=width, offset=0,
                opacity=0.4, marker_line_color="black", marker_line_width=1.3)

    if ylim is not None:
        fig.update_yaxes(range=list(ylim))
    return fig


def plot_riemann_sandwich(x, f_vals, edges, lower_heights, upper_heights, width, ylim=None):
    fig = go.Figure()
    fig.add_scatter(x=x, y=f_vals, mode="lines", name="f(x)")
    fig.add_bar(x=edges[:-1], y=lower_heights, width=width, offset=0, marker_color="steelblue",
                opacity=0.5, name="lower sum", marker_line_color="black", marker_line_width=1.3)

    fig.add_bar(x=edges[:-1], y=upper_heights - lower_heights,
                width=width, offset=0,
                base=lower_heights,
                opacity=0.5, marker_color="salmon", name="gap", marker_line_color="black", marker_line_width=1.3)

    fig.update_layout(barmode="overlay")
    if ylim is not None:
        fig.update_yaxes(range=list(ylim))
    return fig
