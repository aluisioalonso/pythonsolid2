from random import randint
n = ( randint(1,10), randint(1,10), randint(1,10), randint(1,10),
randint(1,10) )

print('os valores sorteados foram: ', end='')

for c in n:
    print(f'{c}', end=' ')

print(f'\no maior numero: {max(n)}')
print(f'o menor numero: {min(n)}')