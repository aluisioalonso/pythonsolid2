expressao = input("Digite a expressão: ")
pilha = []

for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if not pilha:
            print("Erro: parêntese fechado sem correspondente.")
            break
        else:
            pilha.pop()

if not pilha:
    print("Os parênteses estão balanceados.")
else:
    print("Erro: parênteses abertos sem fechamento.")
