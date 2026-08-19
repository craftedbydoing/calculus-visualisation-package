import numpy as np
import streamlit as st

from calc_package.catalog import ALL_SEQUENCES
from calc_package.core.sequences import sample_sequence
from calc_package.plotting.sequences_plotly import plot_sequence

st.markdown(
    "#### Here you can visualize sequences of your liking."
)

# --- controls ---
sequences = ALL_SEQUENCES
seq_name = st.selectbox("Choose your sequence ", list(sequences.keys()))
n_terms = st.slider("#of elements", min_value=1,
                    max_value=200, value=20, step=1)

# --- core ---
entry = sequences[seq_name]
n, a = sample_sequence(entry["f"], n_terms)
fig = plot_sequence(n, a)

# --- plotting ---
st.plotly_chart(fig)
