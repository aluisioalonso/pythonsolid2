from ex108 import moeda

preco = float(input('Digite o preço: R$'))
print(f'a metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'o dobro de {moeda.moeda(preco)} é {moeda.dobro(preco)}')
print(f'Aumentando 10% temos: {moeda.aumento(preco,)}')
