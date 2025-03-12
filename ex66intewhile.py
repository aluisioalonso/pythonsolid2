soma  = 0
cont = 0
while True:
    valor = int(input('digite um valor[999 para parar]: '))
    cont += 1
    if valor == 999:
        break
    soma += valor

print(f'os numeros digitados foram {cont-1} e a soma foi {soma}')