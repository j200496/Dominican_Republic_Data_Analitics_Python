import pandas as pd 
import pypyodbc #pip install pypyodbc
import streamlit as st
import plotly.express as pl

server = 'DESKTOP-5FGC431'
database = 'FastFood'
connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
conn = pypyodbc.connect(connection_string)
sql_query = "select * from Ventas where Estado = 'Activa'"
sq = "select MontoTotal * ITBIS as Total"
df = pd.read_sql(sql_query, conn)
sql2 = df["idventa"]
st.header("Reporte de ventas")
st.metric(label="Total ventas",value=len(sql2),delta= 0.5)
fig = pl.bar(df,x="fecharegistro",y="montototal",title="Test")
st.plotly_chart(fig, use_container_width=True)
st.bar_chart(df,x="montototal",y="fecharegistro")
st.dataframe(df)
