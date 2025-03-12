valor = []
while True:
    valors = int(input('Digite um número: '))

    continuar = ' '

    if valors in valor:
        print('Valor duplicado, não vou adicionar.')
    else:
        valor.append(valors)
        valor.sort()
        print('Valor adicionado com sucesso.')

    while continuar not in 'SN':
        continuar = input('Quer continuar? (S/N): ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'Os valores adicionados foram {valor}')
