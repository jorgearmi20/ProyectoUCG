import streamlit as st
import pandas as pd
st.title("Proyecto Final UCG - Jorge Armijos")
st.header("Propuesta")
st.badge("Sistema")
st.sidebar.title("Parámetros")
st.sidebar.image("python.png")

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)

for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)
