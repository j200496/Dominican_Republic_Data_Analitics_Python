import pandas as pd 
import pypyodbc #pip install pypyodbc
import streamlit as st
import plotly.express as pl
import datetime

# Leer el archivo CSS y aplicarlo
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

server = 'DESKTOP-5FGC431'
database = 'FastFood'
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
conn = pypyodbc.connect(connection_string)
sql_queryv = "select * from Ventas where Estado = 'Activa'"
sql_queryc = "select * from Compras where Estado = 'Credito'"
querytop5 = "select DISTINCT top 5 p.Nombre, d.Cantidad from DetalleVenta d inner join Productos p on p.IdProducto = d.IdProducto order by Cantidad desc"
sq = "select MontoTotal * ITBIS as Total"
df5 = pd.read_sql(querytop5,conn)
df = pd.read_sql(sql_queryv, conn)
dfc = pd.read_sql(sql_queryc,conn)
x = datetime.datetime.now() - datetime.timedelta(days=30)
fechaf = x.date()
compracredito = dfc["idcompra"].count()
st.subheader(f"Top 5 prod mas vendidos desde {fechaf} hasta hoy")
figg = pl.bar(df5,x="nombre",y="cantidad",color="cantidad")
st.plotly_chart(figg,use_container_width=True)
st.dataframe(dfc)
st.metric(label="Compras a credito",value=compracredito)
sql2 = df   ["idventa"]
totventas = df["montototal"].sum()
totalv = pd.to_numeric(totventas)
st.header("Reporte de ventas")
col1,col2 = st.columns(2)
col1.metric(label="Total ventas",value=len(sql2),delta= 0.5)
col2.metric(label="Total produccion",value=totalv)
fig = pl.bar(df,x="fecharegistro",y="montototal",title="Test")
st.plotly_chart(fig, use_container_width=True)
st.bar_chart(df,x="montototal",y="fecharegistro")
st.dataframe(df)
