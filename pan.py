import pandas as pd
import streamlit as st
import plotly.express as px
#Series
data = [100,102,104]
apts = ["Apart1","Apart2","Apart3"]
series = pd.Series(data,index=[apts])
#print(series)
#location de value by index
#print(series.iloc[2])
#location de value by label
#print(series.loc["Apart2"])
#filtering by values
#print(series[series > 102])

#DATAFRAMES
dataf = {"Name": ["SpongeBob", "Patrick", "Squidward"],
         "Age":[30,35,50]}
df = pd.DataFrame(dataf)
#Adding a new column
df["Job"] = ["Cook","N/A","Cashier"]
col1,col2 = st.columns(2)
c1,c2 = st.columns(2)
col2.title("Prueba")
c1.metric(label="Number of users",value= len(df["Age"]), border=True)
st.dataframe(df)
fig = px.bar(df, y='Age', x='Name', title='Test', text_auto=True, color='Age')
st.plotly_chart(fig, use_container_width=True)