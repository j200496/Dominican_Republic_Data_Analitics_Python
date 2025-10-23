import streamlit as st 
import pandas as pd
import nump as np
import plotly.express as pl

st.title("Medallas olimpicas")
ruta_excel = r"C:\Users\User\Desktop\Python\Data\olimpic_medals.xlsx"
def CargarDatos():
    return pd.read_excel(ruta_excel)

df= CargarDatos()
ano = sorted(df["Year"].unique())
medalla = sorted(df["Medal"].dropna().unique())

filtro = st.sidebar.selectbox("Filtrar por año",ano, index=None,placeholder="Seleccione por año")
filtro2 = st.sidebar.selectbox("Filtrar medalla",medalla, index=None,placeholder="Seleccione por medalla")
#Replace empty data with the avg of the column
#x = df["Height"].mean()
#df.fillna({"Height":x}, inplace=True)
medals= df[df["Medal"]  == "Gold"]
medals_count = medals.groupby("City").size().reset_index(name="Medal")
fg = pl.bar(medals_count,x="City",y="Medal",title="Medallas por ciudades", text_auto=True, color="City")
st.plotly_chart(fg,use_container_width=True)
y = df["Height"].mode()[0]
df.fillna({"Height":y},inplace=True)
df.drop_duplicates(inplace=True)

if filtro and filtro2:
 df_filtered = df[df["Year"] == filtro] & df[df["Medal"] == filtro2]
 st.dataframe(df_filtered)
else:
   st.dataframe(df)
 

archivo = st.file_uploader("Sube tu archivo Excel", type=["xlsx", "xls"])
if archivo is not None:
    df1 = pd.read_excel(archivo)
    st.dataframe(df1)