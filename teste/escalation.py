import pandas as pd 
import streamlit as st
import plotly.express as px 


df= pd.read_csv('Escalations.xlsx - Data.csv', sep=',')

st.set_page_config(page_title='Dashboard Tickets', layout='wide')

# converter para data
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
df = df.dropna(subset=['Timestamp'])
df = df.sort_values('Timestamp')

# criar colunas
df['Month'] = df['Timestamp'].dt.to_period('M').astype(str)
df['Day'] = df['Timestamp'].dt.date.astype(str)

# filtro por mês
month = st.sidebar.selectbox('Select Month:', sorted(df['Month'].unique()))
df_month = df[df['Month'] == month]

# filtro por dia
day = st.sidebar.selectbox('Select Day:', sorted(df_month['Day'].unique()))
df_filtered = df_month[df_month['Day'] == day]





st.dataframe(df_filtered)   


col1,col2, col3  = st.columns(3)
col4, col5, col6 = st.columns(3)


# contar tickets por data
tickets_total = df_filtered.groupby(['Timestamp','ASA']).size().reset_index(name='Total')

# gráfico
fig_date = px.bar(
    tickets_total,
    x='Timestamp',
    y='Total',
    title='Cases per Day',
    color='ASA',
    barmode='group',
)

col1.plotly_chart(fig_date, use_container_width=True)
