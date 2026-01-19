import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Sample Dashboard")
st.subheader("Overview")

dataframe = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

st.dataframe(dataframe)