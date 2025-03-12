from ex109 import moeds

preco = float(input('Digite o preço: R$'))
print(f'a metade de {moeds.moeda(preco)} é {moeds.metade(preco, True)}')
print(f'o dobro de {moeds.moeda(preco)} é {moeds.dobro(preco, True)}')
print(f'Aumentando 10% temos: {moeds.aumento(preco, False)}')
