import pandas as pd
import pyodbc 
import streamlit as st
import plotly.express as pl



server = 'DESKTOP-5FGC431'
database = 'Candidate' 
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)
query = "select Nombre,Telefono,Direccion,Cedula,Provincia from Personas where Borrado = 'No'"
df = pd.read_sql(query,conn)
st.header("Lista de miembros")
a,b = st.columns(2)
prov = df["Provincia"]
miembros = df["Nombre"].unique()
sel = st.selectbox(
    "Filtrar por provincia",
    options=prov,
    index=None,
    placeholder="Selecciona una provincia"
)
nombre = st.text_input("Buscar", placeholder="Buscar por nombre")
if nombre:
    # Filtrar con coincidencias parciales e ignorando mayúsculas
    df_filtrado = df[df["Nombre"].str.contains(nombre, case=False, na=False)]
    st.dataframe(df_filtrado)

df_filtrado = df[df["Provincia"] == sel]
a.metric(label="Total de miembros", value= len(miembros), border=True)
b.metric(label="Cantidad de miembros seleccionados", value= len(df_filtrado),border=True)
if sel:
    df_filtrado = df[df["Provincia"] == sel]
    st.dataframe(df_filtrado)
else:
    st.dataframe(df)
st.subheader("Graficos por provincias")
fg = pl.bar(df,x="Provincia")
st.plotly_chart(fg,use_container_width=True)

