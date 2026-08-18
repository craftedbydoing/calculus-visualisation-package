import numpy as np
import streamlit as st

from calc_package.core.sequences import sample_sequence
from calc_package.plotting.sequences_plotly import plot_sequence

sequences = {
    "1/n": {"f": lambda n: 1/n, "L": 0},
    "3-1/n": {"f": lambda n: 3-1/n, "L": 3},
    "2^n": {"f": lambda n: 2**n, "L": "inf"},
    "sin(n)": {"f": lambda n: np.sin(n), "L": "DNE"},
}
# --- controls ---

seq_name = st.selectbox("Posloupnosti", list(sequences.keys()))
n_terms = st.slider("Počet členů", min_value=1,
                    max_value=70, value=10, step=1)

# --- core ---
entry = sequences[seq_name]
n, a = sample_sequence(entry["f"], n_terms)

fig = plot_sequence(n, a)

# --- plotting ---
st.plotly_chart(fig)
