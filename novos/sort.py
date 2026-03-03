produtos=['arroz','feijão','macarrão','carne','frango  ','Iphone','queijo','manteiga','pão','bolo']
#ordenar a lista em ordem alfabética
produtos.sort(key=str.lower)  #sort nao coloca em alfabetico, coloca na tabela asscii, entao tem que usar o key=str.lower para colocar em ordem alfabetica

print(produtos)