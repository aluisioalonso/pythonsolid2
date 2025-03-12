def maior(*num):
    ler = len(num)
    if ler > 1 and num != 0:
        print(num, f'Foram informados {ler} valores ao todo')

    elif min(num) == 0:
        print(num, f'Foram informados 0 valores ao todo')

    print(f'o maior valor foi {max(num)}')
maior(9,5,2)
maior(4,7,0,3,1)
maior(0)