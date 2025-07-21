import pandas as pd
import plotly.graph_objects as go   
import streamlit as st
import time

 
car_data = pd.read_csv('vehicles_us.csv')

st.title("Estudio de Vehiculos en US")

page_names = ['Histograma', 'Dispersion']

page = st.radio('Seleccione el tipo de grafico', page_names)

if page == 'Histograma':
    st.subheader('Histograma')

    with st.spinner("Por favor espere...", show_time=True):
        fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
        fig.update_layout(title_text='Distribución del Odómetro')
        time.sleep(2)
        st.plotly_chart(fig, use_container_width=True)


if page == 'Dispersion':
    st.subheader('Grafica de Dispersion')

    with st.spinner("Por favor espere...", show_time=True):
      fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
      fig.update_layout(title_text='Relación entre Odómetro y Precio')
      time.sleep(2)
      st.plotly_chart(fig, use_container_width=True) 
