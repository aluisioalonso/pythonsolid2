temp = []
princ = []
mai = men = 0

while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N]'))
    if resp in 'Nn':
        break

print(f'os dados foram {princ}')
print(f'ao todo, voce cadastrou {len(princ)} pessoas')
print(f'o mais pesado pesa {mai}KG.', end= '')
for p in princ:

    if p[1] == mai:
        print(f'{p[0]}...', end='')
print(f'\no mais leve pesa {men}KG. ', end='')
for c in princ:

    if c[1] == men:
        print(f'{c[0]}...', end='')