listagem = ('carne', 30, 'frango', 25)
print('_' * 40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('_' * 40)


for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
