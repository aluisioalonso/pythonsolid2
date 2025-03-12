tupla = (
 int(input('digite um numero')),
 int(input('digite um numero')),
 int(input('digite um numero')),
 int(input('digite o ultimo numero: '))
)

print(f'o valor 9 apareceu {tupla.count(9)}')

if 3 in tupla:
    print(f'o valor 3 foi digitado na posisao {tupla.index(3)+1}')
else:
    print('o valor 3 nao foi digitado em nenhuma posicao')
print('os valores par encontrados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

