import numpy as np
import streamlit as st

from calc_package.core.sequences import sample_sequence
from calc_package.plotting.sequences_plotly import plot_sequence
from calc_package.catalog import SEQUENCES

# --- controls ---
sequences = SEQUENCES
seq_name = st.selectbox("Posloupnosti", list(sequences.keys()))
n_terms = st.slider("Počet členů", min_value=1,
                    max_value=70, value=20, step=1)

# --- core ---
entry = sequences[seq_name]
st.latex(entry["latex"])
n, a = sample_sequence(entry["f"], n_terms)

fig = plot_sequence(n, a)

# --- plotting ---
st.plotly_chart(fig)
