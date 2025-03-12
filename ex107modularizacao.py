from ex107 import moedas

preco = float(input('Digite o preço: R$'))
print(f'a metade de {preco} é {moedas.metade(preco)}')
print(f'o dobro de {preco} é {moedas.dobro(preco)}')
print(f'Aumentando 10%, temos: {moedas.aumento(preco)}')
print(f'Reduzindo 13%, temos:  {moedas.reducao(preco)}')