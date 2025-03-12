while True:
    cont = 0
    print('-' * 70)
    valor = int(input('digite um numero para saber a tabuada[digite um numero negativo para sair]: '))
    print('-' * 70)
    if valor < 0:
        break

    while cont <= 10:
        print(f'{valor} x {cont} = {cont * valor}')
        cont += 1


print('PROGRAMA TABUADA ENCERRADO, Volte sempre')