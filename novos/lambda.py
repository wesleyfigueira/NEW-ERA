


imposto = 0.3
 
entrada = float(input("Digite o valor do salário: "))


'''def funcao(entrada):
    return entrada * imposto'''

minha_funcao = lambda entrada: entrada+(entrada * imposto)

print("O valor do imposto é: ", minha_funcao(entrada))