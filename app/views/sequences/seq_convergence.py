import numpy as np
import streamlit as st

from calc_package.catalog import SEQUENCES
from calc_package.core.sequences import find_N_for_limit, sample_sequence
from calc_package.plotting.sequences_plotly import (
    plot_convergence_plotly,
    plot_sequence,
)

st.markdown(r"""
            #### Definition in mathy terms
            :blue-background[
            $\forall\varepsilon > 0 \quad \exists N > 0: \quad$ $a_n\in (L-\varepsilon, L+\varepsilon) \quad$ for all $\quad n>N$]
            """)
st.markdown(r"""
            #### Definition in plain words
            A sequence $a_n$ is converging to $L\in\mathbb{R}$ if:
            
            Give me any $\varepsilon > 0$ you want and I guarantee you that I find $N\in \mathbb{N}$ with a property that:
            all elements from $N$ onwards (that is $a_N, a_{N+1}, a_{N+2}, \ldots$) are at most $\varepsilon$ far from the number $L$ (distance wise).
            """)

st.markdown("""
            And so casually said we are 
            """)


EPS_MAX = 1.0
sequences = SEQUENCES
# --- controls ---
seq_name = st.selectbox("Choose your sequence ", list(sequences.keys()))
n_terms = st.slider("#of elements", min_value=1,
                    max_value=200, value=20, step=1)
eps = st.slider(r"$\varepsilon$", min_value=0.01,
                max_value=EPS_MAX, value=0.5, step=0.01)

# --- core ---
entry = sequences[seq_name]
L = entry["L"]
n, a = sample_sequence(entry["f"], n_terms)
N = find_N_for_limit(n, a, L, eps)

y_max = np.max([np.max(a), L + EPS_MAX])
y_min = np.min([np.min(a), L - EPS_MAX])
pad = 1 if (y_max - y_min) < 0.5 else (y_max - y_min) * 0.1
ylim = (y_min - pad, y_max + pad)

# --- plotting ---
st.markdown(rf"""
            Nepřítel zvolil :red-background[**$\varepsilon$ = {eps:.2f}**].

            Stačí volit :green-background[**$N = {N}$**].
            """)
fig = plot_convergence_plotly(n, a, L, eps, N, ylim)
st.plotly_chart(fig)
