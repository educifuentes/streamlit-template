"""
Data Viewer page - Display and filter transactions dataframe.
"""
import pandas as pd
import streamlit as st


# Page content
st.title("📊 Data Viewer")

st.dataframe(pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
}), width='stretch')
