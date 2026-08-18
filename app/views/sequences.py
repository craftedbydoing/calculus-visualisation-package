import numpy as np
import streamlit as st

from calc_package.core.sequences import find_N_for_limit, sample_sequence
from calc_package.plotting.sequences_plotly import plot_convergence_plotly, plot_sequence

EPS_MAX = 1.0
sequences = {
    "1/n": {"f": lambda n: 1/n, "L": 0},
    "3-1/n": {"f": lambda n: 3-1/n, "L": 3},
    "2^n": {"f": lambda n: 2**n, "L": "inf"},
    "sin(n)": {"f": lambda n: np.sin(n), "L": "DNE"},
}
# --- controls ---
with st.sidebar:
    seq_name = st.selectbox("Posloupnosti", list(sequences.keys()))
    eps = st.slider(r"$\varepsilon$", min_value=0.01,
                    max_value=EPS_MAX, value=0.5, step=0.01)
    n_terms = st.slider("Počet členů", min_value=1,
                        max_value=70, value=3, step=1)

# --- core ---
entry = sequences[seq_name]
L = entry["L"]
n, a = sample_sequence(entry["f"], n_terms)
N = find_N_for_limit(n, a, L, eps)

if N:
    y_max = np.max([np.max(a), L + EPS_MAX])
    y_min = np.min([np.min(a), L - EPS_MAX])
    pad = 1 if (y_max - y_min) < 0.5 else (y_max - y_min) * 0.1
    ylim = (y_min - pad, y_max + pad)
    fig = plot_convergence_plotly(n, a, L, eps, N, ylim)
else:
    fig = plot_sequence(n, a)

# --- plotting ---
st.markdown(r"""
            ### Definition
            :blue-background[
                $\forall\varepsilon > 0 \quad \exists N > 0: \quad$ $a_n\in (L-\varepsilon, L+\varepsilon) \quad$ for all $\quad n>N$]""")

st.markdown(rf"""
            Nepřítel zvolil :red-background[**$\varepsilon$ = {eps:.2f}**].

            Stačí volit :green-background[**$N = {N}$**].
            """)
st.plotly_chart(fig)
