soma = 0
cont_homens = 0
cont_mulheres_menos_20 = 0
total_pessoas = 0

while True:
    print(f'--- {total_pessoas + 1}ª PESSOA ---')

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo (M/F): ').strip().upper()[0]

    soma += idade  # Agora a soma inclui a última pessoa
    total_pessoas += 1

    if sexo == 'M':
        cont_homens += 1
    elif sexo == 'F' and idade < 20:
        cont_mulheres_menos_20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? (S/N): ').strip().upper()[0]

    if continuar == 'N':
        break

# Evitar erro de divisão por zero
media = soma / total_pessoas if total_pessoas > 0 else 0

print(f'\nA média das idades é: {media:.2f}')
print(f'Ao todo, temos {cont_homens} homens cadastrados.')
print(f'Ao todo, temos {cont_mulheres_menos_20} mulher(es) com menos de 20 anos.')

