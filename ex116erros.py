def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero-1)
try:
    x = int(input('digite um numero inteiro positivo para calcular seu fatorial: '))
    res = fatorial(x)
except RecursionError:
    print('nao da para calcular esse numero')
except (ValueError, TypeError):
    print('voce tem que digitar um numero inteiro')
except KeyboardInterrupt:
    print('\no usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'o erro encontrado foi esse: {erro}')
else:
    print(f'o fatorial de {x} é = {res}')