soma = 0
cont = 0
mai_val = 0
men_val = 9999999999999999999999
numero = 0

while numero != -99:
    numero = int(input('Digite um numero: '))
    if numero == -99:
        break

    cont += 1
    soma += numero
    if cont == 1:
        mai_val = numero
        men_val = numero
    else:
        if mai_val <= numero:
            mai_val = numero

        if men_val >= numero:
            men_val = numero

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if continuar == 'S':
        numero = 0
    elif continuar == 'N':
        break
    else:
        print('opcao errada')





media = soma / cont
print(f'a media dos numeros foram: {media}')
print(f'o maior numero foi {mai_val} e o menor foi {men_val}')