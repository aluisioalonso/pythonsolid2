dados = {}
ligol = []

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
tot = 0
for c in range(0, partidas):
    gols = int(input(f'quantos gol na partida {c}? '))
    dados['gols'] = gols
    ligol.append(dados['gols'])
    dados['gols'] = ligol
    tot += gols
    dados['total'] = tot

print(dados)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print(f'O jogador {dados['nome']} jogou {partidas} partidas.')

for i in range(0, partidas):
    print(f'        Na partida {i}, fez {ligol[i]} gols')
print(f'foi um total de {tot} gols')