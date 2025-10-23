import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
from sqlalchemy import create_engine
def obtener_datos():
    server = 'DESKTOP-5FGC431'
    database = 'FastFood'
    
    # Cadena de conexión usando SQLAlchemy con el driver ODBC 17
    connection_string = (
        f"mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    engine = create_engine(connection_string)
    query = "SELECT * from Ventas"
    df = pd.read_sql(query, engine)
    return df


@st.cache_data
def cargar_datos():
    df = obtener_datos()
    df['FechaRegistro'] = pd.to_datetime(df['FechaRegistro'], errors='coerce')
    return df

df = cargar_datos()

# --- 3. Filtro por año ---
años = sorted(df['FechaRegistro'].dt.year.dropna().unique())
año_sel = st.sidebar.selectbox("Seleccionar año:", años)
fecha_sel = st.date_input("Filtrar por fecha (opcional)")

df_filtrado = df[df['FechaRegistro'].dt.year == año_sel]

if fecha_sel:
    df_filtrado = df_filtrado[df_filtrado['FechaRegistro'].dt.date == fecha_sel]


st.dataframe(df_filtrado)
# --- 4. Mostrar tabla ---
st.subheader(f"Ventas del año {año_sel}")
st.dataframe(df_filtrado, use_container_width=True)

# --- 5. Gráfico de barras por mes ---
df_filtrado['Mes'] = df_filtrado['FechaRegistro'].dt.month_name()
fig = px.bar(df_filtrado, x='Mes', y='TotalITBIS', title=f"Ventas por mes - {año_sel}", text_auto=True)
st.plotly_chart(fig, use_container_width=True)

# --- 6. (Opcional) Gráfico por producto ---
if 'Producto' in df.columns:
    fig2 = px.pie(df_filtrado, names='Cliente', values='TotalVenta', title="Ventas por cliente")
    st.plotly_chart(fig2, use_container_width=True)
