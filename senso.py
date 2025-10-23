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
fig.update_layout(yaxis={'categoryorder':'total ascending'}) 
fig.update_layout(width=1500)
st.plotly_chart(fig, use_container_width=True)
fig3 = px.pie(df_sorted,values="Total",names="Provincia",title="Porcentage de poblacion por provincia",color="Provincia")

c1,c2 = st.columns(2)
sur = df[df["Provincia"].isin(["Azua", "Barahona","Bahoruco","Pedernales",
        "Peravia","Elías Piña","San Juan","San José de Ocoa","San Cristóbal","Independencia"])]["Total"].sum()

norte = df[df["Provincia"].isin(["Santiago","Duarte","Puerto Plata","Samaná","María Trinidad Sánchez",
         "Valverde","Santiago Rodríguez","Hermanas Mirabal","Monseñor Nouel","Sánchez Ramírez","Monte Cristi","Monseñor Nouel",
                                "La Vega","Espaillat","Dajabón"])]["Total"].sum()

este = df[df["Provincia"].isin(["La Romana","Hato Mayor","Distrito Nacional","Santo Domingo",
        "El Seibo","San Pedro de Macorís","La Altagracia","Monte Plata"])]["Total"].sum()

df_regiones = pd.DataFrame({
    "Region":["Este","Sur","Norte"],
    "Poblacion":[este,sur,norte]
})
fig4 = px.bar(df_regiones,x="Region",y="Poblacion",title="Poblacion por region",color="Region")
c1.plotly_chart(fig4,use_container_width=True)

df_sexo = pd.DataFrame({
    "Sexo": ["Hombres", "Mujeres"],
    "Cantidad": [total_hombres, total_mujeres]
})
f = px.pie(df_sexo,values="Cantidad",names="Sexo",title="Porcentage por genero",color="Cantidad")
c2.plotly_chart(f,use_container_width=True)
df_genero = df_filtrado.melt(
    id_vars=["Provincia"], 
    value_vars=["Hombres", "Mujeres"], 
    var_name="Sexo", 
    value_name="Cantidad"
)
#fig2 = px.pie(df_genero, values='Cantidad', names='Sexo', title='Cantidad por genero',color="Cantidad")
#c2.plotly_chart(fig2,use_container_width=True)
romana = df[df["Provincia"].isin(["La Romana"])]["Total"].sum()
samana = df[df["Provincia"].isin(["Samaná"])]["Total"].sum()
ptplata = df[df["Provincia"].isin(["Puerto Plata"])]["Total"].sum()
puntacana = df[df["Provincia"].isin(["La Altagracia"])]["Total"].sum()
nagua = df[df["Provincia"].isin(["María Trinidad Sánchez"])]["Total"].sum()

turistic = pd.DataFrame({
    "Provincias":["La Romana","Samana","Puerto Plata","La Altagracia","Maria Trinidad Sánchez"],
     "Poblacion":[romana,samana,ptplata,puntacana,nagua]
})
fig6 = px.bar(turistic,x="Provincias",y="Poblacion",title="Poblacion de provincias turisticas",color="Poblacion")

mtcristi = df[df["Provincia"].isin(["Monte Cristi"])]["Total"].sum()
dajabon = df[df["Provincia"].isin(["Dajabón"])]["Total"].sum()
elpina = df[df["Provincia"].isin(["Elías Piña"])]["Total"].sum()
indep = df[df["Provincia"].isin(["Independencia"])]["Total"].sum()
pedern = df[df["Provincia"].isin(["Pedernales"])]["Total"].sum()

fronterizas = pd.DataFrame({
      "Provincias":["Monte Cristi","Dajabon","Elias Piña","Independencia","Pedernales"],
     "Poblacion":[mtcristi,dajabon,elpina,indep,pedern]
})
fig7 = px.bar(fronterizas,x="Provincias",y="Poblacion", title="Poblacion de provincias fronterizas",color="Poblacion")
st.plotly_chart(fig6,use_container_width=True)
st.plotly_chart(fig7,use_container_width=True)
st.plotly_chart(fig3,use_container_width=True)


