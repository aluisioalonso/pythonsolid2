from ex112.cursoemvideo import moeda
from ex112.cursoemvideo.dado import leiaDinheiro

preco = leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 80)
