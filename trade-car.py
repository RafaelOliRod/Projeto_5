import streamlit as st
import pandas as pd
import plotly.express as px

df_cars = pd.read_csv('datasets/vehicles.csv')

st.header('TRADE CAR - Análise de Veiculos')

st.write("Tabela de Vendas")
st.write(df_cars)


def extract_manufacturer(model):
    return model.split()[0]


# Criando uma nova coluna 'manufacturer' no DataFrame
df_cars['manufacturer'] = df_cars['model'].apply(extract_manufacturer)

# Exibindo o novo DataFrame
df_manufacturer = df_cars[['manufacturer']]

# Contar a frequência de cada fabricante
manufacturer_counts = df_manufacturer['manufacturer'].value_counts()

# Criar um DataFrame com os valores e os índices
df_manufacturer_counts = pd.DataFrame(
    {'manufacturer': manufacturer_counts.index, 'count': manufacturer_counts.values})


# Dividir a tela em duas colunas
col1, col2 = st.columns(2)

# Adicionar botão de histograma à primeira coluna
with col1:
    hist_button = st.button('Criar histograma')

# Adicionar botão de dispersão à segunda coluna
with col2:
    disp_button = st.button('Criar gráfico de disperção')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(df_cars, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Gráfico de disperção para o conjunto de dados de anúncios de vendas de carros')
    # criar um gráfico
    fig = px.scatter(df_cars, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

st.write("")
st.write("")

st.markdown('<h3>Condição do Veículo x Ano de Fabricação</h3>',
            unsafe_allow_html=True)
# Remover linhas com valores ausentes
hist_data = df_cars[['condition', 'model_year']].dropna()
fig = px.histogram(hist_data, x='model_year', color='condition')
st.plotly_chart(fig)


# Dividir a tela em duas colunas
col1, col2 = st.columns(2)

# Adicionar botão de histograma à primeira coluna
with col1:
    manufact_button = st.button('Gráfico por Fabricante')

# Adicionar botão de dispersão à segunda coluna
with col2:
    tp_button = st.button("Gráfico por Tipo de Veículo")

if manufact_button:  # se o botão for clicado
    # Plotar gráficos de pizza
    fig = px.pie(df_manufacturer_counts, values='count',
                 names='manufacturer', title='Distribuição de Fabricantes')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if tp_button:
    # Criar o gráfico de pizza
    type_counts = df_cars['type'].value_counts()
    fig = px.pie(names=type_counts.index, values=type_counts.values,
                 title='Distribuição por Tipo de Veículo')
    st.plotly_chart(fig)

st.write("")
st.write("")

st.markdown('<h3>Compare a distribição de preços entre os Fabricantes</h3>',
            unsafe_allow_html=True)

# Criar duas caixas de seleção
selected_manufacturer_1 = st.multiselect(
    'Selecione fabricantes 1:', df_manufacturer['manufacturer'].unique())
selected_manufacturer_2 = st.multiselect(
    'Selecione fabricantes 2:', df_manufacturer['manufacturer'].unique())

# Filtrar DataFrame com base nos fabricantes selecionados
filtered_df = df_cars[df_cars['manufacturer'].isin(
    selected_manufacturer_1 + selected_manufacturer_2)]

# Verificar se ambos os fabricantes foram selecionados
if len(selected_manufacturer_1) > 0 and len(selected_manufacturer_2) > 0:
    # Adicionar marcador de opção para normalizar o histograma
    histnorm_option = st.checkbox('Normalizar histograma')

    # Criar gráfico de distribuição de preços
    fig = px.histogram(filtered_df, x='price', color='manufacturer',
                       title='Distribuição de Preços por Fabricante',
                       histnorm='percent' if histnorm_option else None)
    st.plotly_chart(fig)
else:
    st.write('Selecione pelo menos um fabricante para comparar.')
