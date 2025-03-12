def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o cálculo.
    :return: O valor do fatorial de num.
    """
    fat = 1

    if show:
        print(f'Calculando {num}! = ', end='')

    for c in range(num, 0, -1):
        fat *= c
        if show:
            print(c, end=' ')
            print('x ' if c > 1 else '= ', end='')

    return fat


print(fatorial(5, show=False))




