from datetime import date


def voto(n= 0):
    ano = date.today().year
    idade = ano - n

    if 16 <= idade < 18 or idade >= 65:
        print('Voce nao é obrigado a votar!')
    elif idade >= 18:
        print('Voce e obrigado a votar!')
    elif idade < 0:
        print('idade inexistente')
    elif idade < 16:
        print('voce nao pode votar')

    return idade

nasc = voto(int(input('digite o ano que vc nasceu: ')))
print(f'voce tem {nasc} anos de idade.')