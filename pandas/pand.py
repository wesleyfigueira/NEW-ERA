import pandas as pd




vendas_df =pd.read_csv('contoso - Vendas - 2017.csv',sep=';')


##print(vendas_df[:5])

lista_clientes = vendas_df['ID Cliente']

print(lista_clientes)