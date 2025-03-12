from datetime import date
ano = date.today().year
dados = {}

while True:

    dados['nome'] = str(input('Nome: '))
    ano_nasc = int(input('Ano de nascimento: '))
    dados['idade'] = ano - ano_nasc

    dados['ctps'] = int(input('Carteira de trabalho (0 nao tem): '))

    if dados['ctps'] == 0:
        break

    else:
        dados['contratacao'] = int(input('ano de contratacao: '))
        dados['salario'] = float(input('Salario: '))
        apos = dados['contratacao'] - ano_nasc
        dados['aposentadoria'] = apos + 35
        break

for v, k in dados.items():
    print(f'{v} tem o valor de {k}')



