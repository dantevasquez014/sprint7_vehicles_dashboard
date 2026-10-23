import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
# Nota: Ahora usamos 'vehicles_us.csv' sin '../' porque app.py está en la misma carpeta que el archivo de datos.
car_data = pd.read_csv('vehicles_us.csv')

# --- Encabezado de la aplicación ---
st.header('Análisis de Venta de Coches - Cuadro de Mandos')
st.write('Bienvenido/a al explorador de datos de vehículos. Selecciona qué gráfico deseas visualizar.')

# --- 1. Botón para construir un histograma ---
hist_button = st.button('Construir Histograma de Odómetro')

if hist_button:
    st.write(
        'Generando un histograma para el kilometraje (odómetro) de los vehículos...')
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Kilometraje')
    # Mostrar el gráfico interactivo en la aplicación
    st.plotly_chart(fig_hist, width='stretch')

# --- 2. Casilla de verificación para gráfico de dispersión ---
# Utilizamos una casilla de verificación (checkbox) como alternativa sugerida
scatter_checkbox = st.checkbox(
    'Mostrar gráfico de dispersión: Odómetro vs. Precio')

if scatter_checkbox:
    st.write(
        'Generando un gráfico de dispersión que compara el kilometraje con el precio...')
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig_scatter = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig_scatter.update_layout(title_text='Relación entre Kilometraje y Precio')
    # Mostrar el gráfico interactivo en la aplicación
    st.plotly_chart(fig_scatter, width='stretch')
