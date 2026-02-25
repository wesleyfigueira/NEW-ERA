import pandas



caminho=r"C:\Users\wesle\Downloads\Vendas - Dez (3).xlsx"
tabela = pandas.read_excel(caminho)

qtde_produtos = tabela["Quantidade"].sum()
faturamento = (tabela["Valor Final"].sum()) 
tipo_produto = (tabela["Produto"] == "Pulseira Estampa").sum()


print(f"Quantidade de produtos vendidos: {qtde_produtos}")
print(f"Faturamento total: R${faturamento}")    
print(f"Tipos de produtos vendidos: {tipo_produto}")