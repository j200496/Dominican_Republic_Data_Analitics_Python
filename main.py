import streamlit as st
import pandas as pd

st.title("Data frame")

df = pd.DataFrame({
    "Name":['Alice','Bob','David','Maria'],
    "Age":[20,52,35,46]
})
st.dataframe(df)
st.subheader("Metrics")
st.metric(label="Total de rows",value=len(df))
df2 = pd.DataFrame({
    "Country":['USA','Russia','China','Canada'],
    "Population in millions":[400,1200,1600,80]
})
st.dataframe(df2)
st.subheader("Fecha")
st.date_input("Filtrar por fecha")