import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('Data/poblacion_rd_csv.txt')
cl1,cl2 = st.columns(2)
cl1.title("Población Dominicana según el último censo 2022")
cl2.image("Images/band.png", caption="República Dominicana", width=300)
st.link_button("Fuente: Oficina nacional de Estadistica (ONE)","https://www.one.gob.do/datos-y-estadisticas/")
st.markdown(":blue[Analis de datos creado por Joel Diaz con python,streamlit y plotly express.]")
provincias = df["Provincia"].unique()
filt = st.selectbox("Filtrar por provincias", provincias, index=None, placeholder="Filtrar")
df_filtrado = df[df["Provincia"] == filt]

total_hombres = df["Hombres"].sum()
total_mujeres = df["Mujeres"].sum()
ptotal = total_hombres + total_mujeres
rest = total_hombres - total_mujeres
rest2 = total_mujeres - total_hombres

total_hombresf = df_filtrado["Hombres"].sum()
total_mujeresf = df_filtrado["Mujeres"].sum()
ptotalf = total_hombresf + total_mujeresf
restf = total_hombresf - total_mujeresf
rest2f = total_mujeresf - total_hombresf




col1, col2, col3 = st.columns(3)
if filt:
   col1.metric(label="Poblacion total", value=f"{ptotalf:,}",border=True)
   col2.metric(label="Hombres", value=f"{total_hombresf:,}", border=True,delta=restf)
   col3.metric(label="Mujeres", value=f"{total_mujeresf:,}", border=True, delta=rest2f)
else: 
   col1.metric(label="Poblacion total", value=f"{ptotal:,}",border=True)
   col2.metric(label="Hombres", value=f"{total_hombres:,}", border=True,delta=rest)
   col3.metric(label="Mujeres", value=f"{total_mujeres:,}", border=True, delta=rest2)


df_display = df.copy()
df_display["Total"] = df_display["Total"].apply(lambda x: f"{x:,}")
df_display["Hombres"] = df_display["Hombres"].apply(lambda x: f"{x:,}")
df_display["Mujeres"] = df_display["Mujeres"].apply(lambda x: f"{x:,}")

if filt:

    df_filtrado = df_display[df_display["Provincia"] == filt]
    st.dataframe(df_filtrado)
else:
 
    st.dataframe(df_display)

df_sorted = df.sort_values(by="Total", ascending=False)

fig = px.bar(
    df_sorted,
    x="Provincia",
    y="Total",
    orientation='v',
    title="Población por provincia",
    text_auto=True,
    height=500, 
     width=2000 
)
fig3 = px.pie(df_sorted,values="Total",names="Provincia",title="Porcentage de poblacion por provincia",color="Provincia")
fig.update_layout(yaxis={'categoryorder':'total ascending'}) 
fig.update_layout(width=1500)
c1,c2 = st.columns(2)
c1.plotly_chart(fig, use_container_width=True)
df_sexo = pd.DataFrame({
    "Sexo": ["Hombres", "Mujeres"],
    "Cantidad": [total_hombres, total_mujeres]
})
fig2 = px.pie(df_sexo, values='Cantidad', names='Sexo', title='Cantidad por genero',color="Sexo")
c2.plotly_chart(fig2,use_container_width=True)
st.plotly_chart(fig3,use_container_width=True)