matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar = mair = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}] , [{c}]: '))


for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:>5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

print(f'a soma de todos os valores pares da matriz é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'a soma do valor da terceira coluna é {scol}')
for c in range(0,3):
   if c == 0:
       mair = matriz[1][c]
   elif matriz[1][c] > mair:
       mair =matriz[1][c]
print(f'o maior valor da segunda linha é {mair}')