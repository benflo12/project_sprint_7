import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
     

# Botón para gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Gráfico de dispersión: relación entre kilometraje y precio')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)

#Boton para grafico de barras
bar_button = st.button('Construir gráfico de barras') # crear un botón
if bar_button:
    st.write('Grafico  de barras: relacion entre el año del modelo y el precio')

    bar = px.bar(car_data, x="model_year", y="price")

    st.plotly_chart(bar, use_container_width=True)
