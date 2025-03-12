numero = []

for c in range(0,5):
    num = (int(input('digite um numero: ')))
    posicao = 0
    for index, valor in enumerate(numero):
        if valor > num:
            break
        posicao += 1

    numero.insert(posicao, num)

    if posicao == len(numero) - 1:
        print('esse numero foi adicionado no final da lista')
    else:
        print(f'o numero {num} foi adicionado na posicao {posicao}')

print(f'os valores digitados em ordem foram: {numero}')




