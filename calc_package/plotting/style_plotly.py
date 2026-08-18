import plotly.io as pio
import plotly.graph_objects as go

CURVE   = "#4A4038"
ACCENT  = "#C2662D"
FILL    = "#E0A44C"
NEUTRAL = "#9A8F80"

pio.templates["calc-package"] = go.layout.Template(
    layout=dict(
        colorway=[CURVE, ACCENT, FILL, NEUTRAL],
        paper_bgcolor="#FAF7F2",
        plot_bgcolor="#FAF7F2",
        font=dict(color="#3D362F", size=14),
        xaxis=dict(gridcolor="#E0D6C8", zerolinecolor="#C8BCA9",
           tickfont=dict(color="#6B6155"), title_font=dict(color="#3D362F")),
        yaxis=dict(gridcolor="#E0D6C8", zerolinecolor="#C8BCA9",
                tickfont=dict(color="#6B6155"), title_font=dict(color="#3D362F")),
        margin=dict(l=50, r=30, t=50, b=50),
    )
)
pio.templates.default = "calc-package"