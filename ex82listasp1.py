valor = []
valor_par = []
valor_impar = []
while True:
    num = (int(input('digite um valor: ')))
    if num % 2 == 0:
        valor_par.append(num)
    else:
        valor_impar.append(num)

    valor.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? (S/N): ').strip().upper()

    if continuar == 'N':
        break

print(f'a lista completa foi {valor}')
print(f'a lista de pares foi {valor_par}')
print(f'a lista de impares foi {valor_impar}')