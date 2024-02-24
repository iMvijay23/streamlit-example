import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Function to count CpG in a DNA sequence
def count_cpg(dna_sequence):
    return dna_sequence.upper().count('CG')

"""
# DNA CpG Site Counter

This tool counts the number of CpG sites in a given DNA sequence. CpG sites are regions in DNA where a cytosine nucleotide is followed by a guanine nucleotide in the linear sequence of bases along its 5' → 3' direction.
"""

# User input for DNA sequence
dna_sequence = st.text_area("Enter DNA Sequence", "CGATCGCGGTCG")

# Counting CpG sites
cpg_count = count_cpg(dna_sequence)

# Displaying the result
st.write(f"The number of CpG sites in the given sequence is: {cpg_count}")
