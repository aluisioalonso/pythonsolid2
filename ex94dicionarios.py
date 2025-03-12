dados = {}
dado = []
cont = 0
while True:
    dados['nome'] = str(input('Nome: '))
    cont += 1
    dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    resposta = str( input ('Quer continuar? [S/N]'))
    dado.append(dados.copy())
    if resposta in 'Nn':
        break

print(f'O grupo tem {cont} pessoas.')

media = 0
for c in range(cont):
    media += dado[c]['idade']
media /= cont

print(f'A média das idades é de {media:.2f} anos')


print('As mulheres cadastradas foram:', end=' ')
for i in range(cont):
    if dado[i]['sexo'] == 'F':
        print(dado[i]['nome'], end=' ')
print()


print('Lista de pessoas com idade acima da média:')
for i in range(cont):
    if dado[i]['idade'] > media:
        for k, v in dado[i].items():
            print(f'{k} = {v};', end=' ')
