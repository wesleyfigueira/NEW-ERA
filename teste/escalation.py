import pandas as pd 
import streamlit as st
import plotly.express as px 


df= pd.read_csv('Escalations.xlsx - Data.csv')

print(df)

st.dataframe(df)   

# converter para data
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# remover datas inválidas
df = df.dropna(subset=['Timestamp'])

# ordenar
df = df.sort_values('Timestamp')

# criar coluna de mês
df['Month'] = df['Timestamp'].dt.to_period('M').astype(str)

# filtro no Streamlit
month = st.sidebar.selectbox('Select Month:', sorted(df['Month'].unique()))

# dataframe filtrado
df_filtered = df[df['Month'] == month]




