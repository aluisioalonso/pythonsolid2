dados = {}

dados['nome'] = str(input('digite seu nome: '))
dados['media'] = float(input('digite sua media: '))

print(f'nome é igual a {dados["nome"]}')
print(f'media é igual a {dados["media"]}')
if dados['media'] >= 7:
    print('a situacao e igual a Aprovado')
else:
    print('a situacao é igual a Reprovado')
