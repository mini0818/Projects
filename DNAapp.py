######################
# Import Libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import re

######################
# Page Config
######################

st.set_page_config(page_title="DNA Nucleotide Counter", page_icon="🧬", layout="centered")

######################
# Background Styling (Dark Mode)
######################

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

######################
# Display Image Header
######################

st.image("dna.jpg", use_container_width=True, caption="DNA Structure")

######################
# Title & Description
######################

st.title("🧬 DNA Nucleotide Count Web App")
st.markdown("""
This app allows you to analyze a DNA sequence by calculating:

- The count of each nucleotide (A, T, G, C)
- GC content percentage
- Reverse complement sequence
- Nucleotide distribution charts

---
""")

######################
# Sidebar Options
######################

st.sidebar.header("⚙️ Options")
show_table = st.sidebar.checkbox("Show Count Table", value=True)
show_bar = st.sidebar.checkbox("Show Bar Chart", value=True)
show_pie = st.sidebar.checkbox("Show Pie Chart", value=True)
show_reverse = st.sidebar.checkbox("Show Reverse Complement", value=True)

######################
# Sequence Input Area / File Upload
######################

st.header("📥 Input DNA Sequence")

uploaded_file = st.file_uploader("Upload a text/FASTA file", type=["txt", "fasta"])
default_sequence = """>DNA Query
GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"""

if uploaded_file is not None:
    sequence = uploaded_file.read().decode("utf-8")
else:
    sequence = st.text_area("Paste your DNA sequence below:", default_sequence, height=200)

# Preprocess sequence: remove headers and newlines
sequence_lines = sequence.splitlines()
sequence = ''.join([line for line in sequence_lines if not line.startswith(">")]).upper()

######################
# Display Processed Sequence
######################

st.subheader("🧾 Cleaned DNA Sequence")
st.code(sequence, language="text")
st.write(f"🔢 Length: **{len(sequence)}** nucleotides")

######################
# Validate Sequence
######################

if not re.fullmatch('[ATGC]*', sequence):
    st.warning("⚠️ The sequence contains characters other than A, T, G, and C.")
    st.stop()

######################
# Nucleotide Count Function
######################

def DNA_nucleotide_count(seq):
    return {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C')
    }

counts = DNA_nucleotide_count(sequence)

######################
# GC Content
######################

gc_content = (counts['G'] + counts['C']) / len(sequence) * 100
st.subheader("🧪 GC Content")
st.write(f"GC Content: **{gc_content:.2f}%**")

######################
# Output: Dictionary
######################

st.subheader("📊 Nucleotide Count")
st.write(counts)

######################
# Table View
######################

if show_table:
    df = pd.DataFrame.from_dict(counts, orient='index', columns=['Count']).reset_index()
    df = df.rename(columns={'index': 'Nucleotide'})
    st.dataframe(df, use_container_width=True)

######################
# Bar Chart (Altair)
######################

if show_bar:
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Nucleotide', sort=None),
        y='Count',
        color='Nucleotide'
    ).properties(
        width=400,
        height=300,
        title="Bar Chart of Nucleotide Counts"
    )
    st.altair_chart(chart, use_container_width=True)

######################
# Pie Chart (Plotly)
######################

if show_pie:
    pie = px.pie(df, names='Nucleotide', values='Count', title='Nucleotide Composition')
    st.plotly_chart(pie, use_container_width=True)

######################
# Reverse Complement
######################

if show_reverse:
    st.subheader("🧬 Reverse Complement Sequence")
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    reverse_comp = ''.join([complement[base] for base in reversed(sequence)])
    st.code(reverse_comp)

######################
# CSV Download
######################

@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode("utf-8")

csv_data = convert_df_to_csv(df)
st.download_button("📥 Download Count as CSV", data=csv_data, file_name="nucleotide_counts.csv", mime="text/csv")
