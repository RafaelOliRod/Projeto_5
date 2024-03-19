import streamlit as st
import pandas as pd
import plotly.express as px

df_cars = pd.read_csv('datasets/vehicles.csv')

st.header('Análise de Veiculos')

print(df_cars.head(20))


def extract_manufacturer(model):
    return model.split()[0]


# Criando uma nova coluna 'manufacturer' no DataFrame
df_cars['manufacturer'] = df_cars['model'].apply(extract_manufacturer)

# Exibindo o novo DataFrame
df_manufacturer = df_cars[['manufacturer']]
print(df_manufacturer)

# Contar a frequência de cada fabricante
manufacturer_counts = df_manufacturer['manufacturer'].value_counts()

# Criar um DataFrame com os valores e os índices
df_manufacturer_counts = pd.DataFrame(
    {'manufacturer': manufacturer_counts.index, 'count': manufacturer_counts.values})

# Plotar gráficos de pizza
fig = px.pie(df_manufacturer_counts, values='count',
             names='manufacturer', title='Distribuição de Fabricantes')
fig.show()


hist_button = st.button('Criar histograma')
disp_button = st.button('Criar gráfico de disperção')


if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(pd_cars, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de disperção para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico
    fig = px.scatter(pd_cars, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
