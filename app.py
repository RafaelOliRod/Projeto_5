import streamlit as st
import pandas as pd
import plotly.express as px

pd_cars = pd.read_csv('datasets/vehicles.csv')
hist_button = st.button('Criar histograma')
disp_button = st.button('Criar gráfico de disperção')

st.header('Análise de Veiculos')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de disperção para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
