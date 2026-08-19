import numpy as np
import streamlit as st

from calc_package.catalog import SEQUENCES
from calc_package.core.sequences import find_N_for_limit, sample_sequence
from calc_package.plotting.sequences_plotly import (
    plot_convergence_plotly,
)

st.markdown(""" 
            Mathematicians love sequences. In particular sequences that are “well behaved”. That means losely this: 
            
            :green-background[No matter how “messy” they are at start, if we wait long enough they settle around a value of equilibria and they never go back!]
            This property is quite handy, since that makes evolution of the sequenece very much predictable.
            """)

st.markdown(r"""
            #### Definition in plain words
            A sequence $a_n$ is converging to $L\in\mathbb{R}$ if:
            
            Give me any real number $\varepsilon > 0$ you want and I guarantee you that I find number $N\in \mathbb{N}$ with a property that
            all elements from $N$ onwards (that is $a_N, a_{N+1}, a_{N+2}, \ldots$) are at most $\varepsilon$-distance away from the number $L$.
            """)

st.markdown(r"""
            #### Little example to make it more concrete
            Suppose $a_n$ converges to $L=3$. Now you throw at me any positive number, say $\varepsilon = 0.6$. Since $a_n$ converges to 3, I can find a position of $N$-th element in the sequence such that all the sequence members from $N$ onwards have values inbetween $(3-0.6, 3+0.6)=(2.4, 3.6)$. To emphasize: *ALL* members from $N$ onwards. Not three members, not 1394 members -- all members. 
            """)
st.markdown(r"""
            #### Definition in mathy terms
            :blue-background[
            $\forall\varepsilon > 0 \quad \exists N > 0: \quad$ $a_n\in (L-\varepsilon, L+\varepsilon) \quad$ for all $\quad n>N$]
            """)

st.markdown(r"""
            #### Actually, it's like a child's game
            Enemy gives you $\varepsilon$. Since the sequence is convergent, you can reply with $N$ with a property described previously. Now he gets mad at you, so he takes from his basket even smaller $\varepsilon$ and throws it at you with cheeky smile. But you smile back and hand him suitable $N$ again! And the fun thing is that no matter how small $\varepsilon$ he throws at you, you are *always* able to find suitable $N$ to throw back. 
            
            *Enemy opens the door and leaves ...*
            """)


st.header("Convergence widget")
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
            The enemy threw :red-background[**$\varepsilon$ = {eps:.2f}**].

            You can reply with :green-background[**$N = {N}$**].
            """)
fig = plot_convergence_plotly(n, a, L, eps, N, ylim)
st.plotly_chart(fig)
