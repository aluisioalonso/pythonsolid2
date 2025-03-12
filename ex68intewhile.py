from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1,11)
    total = jogador + computador
    tipo = ' '

    while tipo == ' ':
        tipo = str(input('Par ou Impar? [P/I]')).strip().lower()[0]
    print(f'voce jogou {jogador} e o computador {computador}. Um total de {total}')

    if tipo == 'p':
        if total % 2 == 0:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'i':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break

    else:
        print('opcao invalida')

    print('vamos jogar novamente')
print(f'GAMER OVER, voce venceu {v} vezes')