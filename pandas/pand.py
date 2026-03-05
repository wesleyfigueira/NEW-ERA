import pandas as pd

vendas_df = pd.read_csv('contoso - Vendas - 2017.csv', sep=';', encoding='latin1')
produtos_df = pd.read_csv('contoso - Cadastro Produtos.csv', sep=';', encoding='latin1')
loja_df = pd.read_csv('contoso - Lojas.csv', sep=';', encoding='latin1')
cliente_df = pd.read_csv('contoso - Clientes.csv', sep=';', encoding='latin1')





## tirar colunas que não serão usadas
cliente_df=cliente_df.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'], axis=1)

print(cliente_df.head())