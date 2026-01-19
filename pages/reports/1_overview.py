import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Sample Dashboard")
st.subheader("Overview")


st.markdown("Hello! este es una data app de prueba y knowledge base")

st.markdown("Local version [Link](http://localhost:8501)")
st.markdown("Deploy en [Streamlit Cloud Link](https://edu-template.streamlit.app/)")
st.markdown("Deploy en [Render Link](https://spendee-dashboard-educifuentes.streamlit.app/)")
st.markdown("Deploy en [Heroku Link](https://spendee-dashboard-educifuentes.streamlit.app/)")


st.subheader("Data")

dataframe = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40],
})

st.dataframe(dataframe)

