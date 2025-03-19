import streamlit as st
import pandas as pd

DATA_URL = '../uber_dataset.csv'
DATE_COLUMN = 'Date/Time'

@st.cache_data(ttl=60)  # Caché válido por 60 segundos
def load_data(number_rows):
    data = pd.read_csv(DATA_URL, nrows=number_rows)
    lowercase = lambda x: str(x).lower()
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    data.columns = data.columns.str.strip().str.lower()  # Eliminar espacios y pasar a minúsculas
    return data

data = load_data(1000) 
st.dataframe(data)

# Asegúrate de que los datos contienen las columnas 'lat' y 'lon' para el mapa
if 'lat' in data.columns and 'lon' in data.columns:
    data = data.dropna(subset=['lat', 'lon'])
    st.map(data)
else:
    st.write("No se encontraron columnas 'lat' y 'lon' para mostrar en el mapa.")
