def leiaNum(msg):
    while True:
        try:
            num = input(msg).strip().replace(',', '.')  
            if num == '':
                print('\033[31mERRO! Digite um número válido.\033[m')
                continue
            if '.' in num:
                return float(num)
            return int(num)
        except ValueError:
            print('\033[31mERRO! Digite um número válido.\033[m')

ni = nr = 0
try:
    ni = leiaNum('Digite um número inteiro: ')
    nr = leiaNum('Digite um número real: ')

except KeyboardInterrupt:
    print('\n\033[31mEntrada interrompida pelo usuário.\033[m')

print(f'Você acabou de digitar o número inteiro {ni} e o número real {nr}')