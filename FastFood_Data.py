import pyodbc
import pandas as pd
import streamlit as st
import plotly.express as px
server = 'DESKTOP-5FGC431'
database = 'FastFood' 
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};DATABASE={database};Trusted_Connection=yes;"
)
conn = pyodbc.connect(conn_str)
query = "select * from Ventas where MontoTotal > 500"
df = pd.read_sql(query,conn)
ventas = df["IdVenta"].sum()
st.header("Ventas dashboard")
st.dataframe(df)
