
carrinho=[]
item=''

while item != 'sair':
    item=input('Digite um item para o carrinho ou "sair" para finalizar: ')
    if item != 'sair':
        carrinho.append(item)   
    else:
        print('Carrinho finalizado!')
        print('Itens no carrinho:')
        for i, item in enumerate(carrinho, start=1):
            print(f'{i}. {item}')   
