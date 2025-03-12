from time import sleep

def contador(a, b):
    for c in range(a, b):
        print(c, end=' ')

        sleep(0.5)


contador(1,11)
print('FIM!')

def contado(a, b, c):
    for c in range(a, b, c):
        print(c, end=' ')
        sleep(0.5)

contado(10, -1, -2)
print('FIM!')


def cont(a, b, c):
    if c == 0:  # Se o passo for 0, ajustamos ele para 1 ou -1
        c = 1 if a < b else -1

    elif c < 0 and a < b:  # Se passo for negativo, mas o início é menor que o fim, corrigimos o passo
        c = abs(c)

    elif c > 0 and a > b:  # Se passo for positivo, mas o início é maior que o fim, corrigimos o passo
        c = -c

    for i in range(a, b + (1 if c > 0 else -1), c):
        print(i, end=' ', flush=True)
        sleep(0.5)

    print('FIM!')

# Entrada do usuário
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

cont(inicio, fim, passo)