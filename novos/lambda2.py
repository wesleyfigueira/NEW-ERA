

preco_tec={'teclado': 100, 'mouse': 50, 'monitor': 300, 'impressora': 200, 'notebook': 1500, 'tablet': 800, 'smartphone': 1200, 'fones de ouvido': 150, 'caixa de som': 250, 'webcam': 80}


def caucular_preco(preco):
    return preco * 1.3


preco_com_imposto = map(caucular_preco , preco_tec.values())

preco_com_imposto2 = map(lambda preco: preco * 1.3, preco_tec.values())


def produtos_caro(preco):
    return preco > 500

produto_caro = filter(produtos_caro, preco_tec.values())

produtos_caro2 = filter(lambda preco: preco > 500, preco_tec.values())


print(list(preco_com_imposto))
print(list(preco_com_imposto2))
print(list(produto_caro))
print(list(produtos_caro2))