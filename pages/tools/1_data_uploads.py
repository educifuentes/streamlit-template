"""
Upload Spendee CSV and sync to Supabase database.
"""
import pandas as pd
import streamlit as st

st.title("Sample Dashboard")
st.subheader("Upload Data")

st.dataframe(pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
}))