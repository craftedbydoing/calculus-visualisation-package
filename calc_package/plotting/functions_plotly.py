import plotly.graph_objects as go


def plot_function(x, y, label=None):
    fig = go.Figure()
    fig.add_scatter(x=x, y=y, mode="lines", showlegend=False)
    return fig


def plot_epsilon_delta(x, y, a, L, eps, delta, hole_x=None, ylim=None):

    fig = plot_function(x, y)

    fig.add_hrect(y0=L-eps, y1=L+eps, fillcolor="darkblue", opacity=0.3)
    fig.add_hline(y=L, line_color="black")
    fig.add_vrect(x0=a-delta, x1=a+delta, fillcolor="lightgreen", opacity=0.2)

    if hole_x is not None:
        fig.add_scatter(x=[hole_x], y=[L], mode="markers",
                        marker={"size": 10, "color": "white",
                                "line": {"width": 2, "color": "black"}},
                        hovertemplate="f není definována v tomto bodě<extra></extra>",
                        showlegend=False)
    if ylim:
        fig.update_yaxes(range=ylim)

    return fig
