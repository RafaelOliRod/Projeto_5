# import streamlit as st
import pandas as pd
import plotly.express as px

df_cars = pd.read_csv('datasets/vehicles.csv')

print(df_car.head(20))


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
