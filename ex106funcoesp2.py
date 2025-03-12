from time import sleep
def escreva(txt):
    soma = len(txt)
    print('~' * (soma + 7))
    print(f'   {txt}')
    print('~' * (soma + 7))

escreva('SISTEMA DE AJUDA PyHELP')
while True:
    fun = str(input('funcao ou biblioteca? ')).strip()
    if fun in 'fimFIMFimfImfIMFImfiMFiM' :
        break
    else:
        escreva(f'acessando o manual do comando {fun}')
        sleep(1)
        print(help(fun))
        sleep(1)

print('Ate logo')