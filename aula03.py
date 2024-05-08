import streamlit as st
import pandas as pd
# import plotly_express as px

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

#grafico = px.pie(df,names='Tipagem' )

# grafico = px.bar(df, x="Linguagem", y="Desenvolvedores", color='Linguagem' )
# st.plotly_chart(grafico)

st.bar_chart(df, x="Linguagem", y="Desenvolvedores")