dados_jogadores = []

while True:
    dados = {}
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    tot = 0
    gols_partidas = []

    for c in range(partidas):
        gols = int(input(f'Quantos gols na partida {c + 1}? '))
        gols_partidas.append(gols)
        tot += gols
    dados['gols'] = gols_partidas
    dados['total'] = tot
    dados_jogadores.append(dados)

    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break


print('\nTabela de Jogadores:')
print(f'{"Posição":<10}{"Nome":<20}{"Gols":<20}{"Total de Gols":<20}')
for i, jogador in enumerate(dados_jogadores):
    print(f'{i + 1:<10}{jogador["nome"]:<20}{str(jogador["gols"]):<20}{jogador["total"]:<20}')


while True:
    posicao = int(input('\nDigite a posição do jogador para ver os detalhes ou 999 para sair: '))

    if posicao == 999:
        print('Saindo...')
        break

    if 1 <= posicao <= len(dados_jogadores):
        jogador = dados_jogadores[posicao - 1]
        print(f'\nDetalhes do jogador {jogador["nome"]}:')
        print(f'Jogou {partidas} partidas.')
        for i, gols in enumerate(jogador['gols']):
            print(f'   Na partida {i + 1}, fez {gols} gols.')
        print(f'Total de gols: {jogador["total"]}')
    else:
        print('Posição inválida! Tente novamente.')
