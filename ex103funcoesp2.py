def ficha(n, g):

    if n == ''.strip():
        if g == ''.strip():
            print('o jogador <desconhecido> fez 0 gols')
        else:
            print(f'o jogador <desconhecido> fez {g} gols')

    elif g == ''.strip():
        g = 0
        print(f'o jogador {n} fez {g} gols')

    else:
        print(f'o jogador {n} fez {g} gols')


nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Numero de gols: ')).strip()
ficha(nome, gols)
