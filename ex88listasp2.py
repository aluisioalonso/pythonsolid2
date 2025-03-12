alunos = []

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    alunos.append([nome,n1,n2])

    resposta = str(input('quer continuar? [S/N]'))
    if resposta in 'Nn':
        break


print("\nBoletim:")
print(f'{"ID":<4}{"Nome":<10}{"Média":>7}')
print('-' * 25)

i = 0
for i, aluno in enumerate(alunos):
    nome = aluno[0]
    media = (aluno[1] + aluno[2]) / 2
    print(f'{i:<4}{nome:<10}{media:>7.2f}')

while True:
    op = int(input('\nDigite o ID do aluno para ver as notas (999 para sair): '))

    if op == 999:
        print("Encerrando...")
        break
    elif 0 <= op < len(alunos):
        print(f'Notas de {alunos[op][0]}: {alunos[op][1]} e {alunos[op][2]}')
    else:
        print('ID inválido. Tente novamente.')




