valor = []
while True:
    num = (int(input('digite um valor: ')))
    valor.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? (S/N): ').strip().upper()

    if continuar == 'N':
        break


valor.sort(reverse= True)
print(f'voce digitou {len(valor)} elementos')
print(valor)
if valor.count(5) in valor:
    print('o valor 5 faz parte da lista!')
else:
    print('o valor 5 nao faz parte da lista')