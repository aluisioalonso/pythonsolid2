lista = []
cont = 0
while cont <= 4:
    lista.append(int(input(f'digite um valor na posicao {cont}: ')))
    cont += 1

print(f'Voce digitou os valores {lista}')
print(f'o maior valor digitado foi {max(lista)} na posicao {lista.index(max(lista)) }')
print(f'o menor valor digitado foi {min(lista)} na posicao {lista.index(min(lista))}')
