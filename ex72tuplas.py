numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze','catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num =  int(input('digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:

        continuar = ' '
        while continuar not in 'SN':
            continuar = input('Quer continuar? (S/N): ').strip().upper()
        if continuar == 'N':
            print(f'voce digitou o numero {numeros[num]}')
            break
        else:
            print(f'voce digitou o numero {numeros[num]}')
    else:
        print('Tente novamente.', end=' ')
