import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Visualización de ejemplo")

st.subheader("Subtitulo")

data={
    "Categoría":["A","B","C","D","E"],
    "Valores":[10,20,30,40,15]
}

df = pd.DataFrame(data)

st.dataframe(df) #Muestro tabla

st.subheader("Grafico sencillo entre lineas")

fig, ax = plt.subplots()
ax.plot(df["Categoría"],df["Valores"],marker="o", linestyle="-",color="b")
ax.set_xlabel("Categoría")
ax.set_ylabel("Valor")
ax.set_title("Tenddencia Valores")

st.pyplot(fig) #Se muestra en streamlit

st.subheader("Grafico de barras")

fig_bar = px.bar(df, x="Categoría", y ="Valores",text="Valores", color = "Categoría",title="Distribución de valores")
st.plotly_chart(fig_bar)