from random import randint
from time import sleep
numeros = []
def sorteia(*num):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(5):
        c = randint(1,10)
        print(c, end=' ')
        sleep(1)
        numeros.append(c)


sorteia()
print('PRONTO!', end=' ')
print()
def somaPar(som):

    for c in range(5):
        if numeros[c] % 2 == 0:
            som += numeros[c]
    print(f'somando todos os valores pares de {numeros}, temos {som}')
    sleep(1)
soma = 0
somaPar(soma)