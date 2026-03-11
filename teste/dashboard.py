import streamlit as st
import pandas as pd
import plotly.express as px     

st.set_page_config(page_title='Dashboard de Vendas', layout='wide')

df = pd.read_csv('supermarket_sales.csv',sep=';', decimal=',')

df['Date'] = pd.to_datetime(df['Date'])
df=df.sort_values(['Date'])   

df['Month'] = df['Date'].apply(lambda x: str(x.year) + '-' + str(x.month))
month =st.sidebar.selectbox('Selecione o mês', df['Month'].unique())


df_filtered = df[df['Month'] == month]


col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)


fig_date= px.bar(df_filtered, x='Date', y='Total', color='City', title='Vendas por Data')
col1.plotly_chart(fig_date,use_container_width=True)


prod_date= px.bar(df_filtered, x='Date', y='Product line', color='City', title='Faturamento por Tipo de Produto',
                  orientation='h')

col2.plotly_chart(prod_date,use_container_width=True )


city_total = df_filtered.groupby('City')['Total'].sum().reset_index()
fig_city = px.bar(df_filtered, x='City', y='Total', color='City', title='Vendas por filial')
col3.plotly_chart(fig_city,use_container_width=True )


fig_kind = px.pie(df_filtered, values='Total',names='Payment', title='Vendas por tipo de cliente')
col4.plotly_chart(fig_kind,use_container_width=True )


city_total = df_filtered.groupby('City')[['Rating']].mean().reset_index()
fig_rating = px.bar(city_total, x='City', y='Rating', color='City', title='Avaliação média por cidade')
col5.plotly_chart(fig_rating, use_container_width=True)