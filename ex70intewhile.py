cont_itens_caros = 0
nome_barato = ''
soma = 0
mais_barato = None

print('-' * 50)
print('Loja Super Baratão')
print('-' * 50)

while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço do produto (R$): '))
    soma += preco

    if preco > 1000:
        cont_itens_caros += 1

    if mais_barato is None or preco < mais_barato:
        mais_barato = preco
        nome_barato = nome

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? (S/N): ').strip().upper()

    if continuar == 'N':
        break

print('-' * 50)
print(f'O total da compra foi R$ {soma:.2f}')
print(f'Temos {cont_itens_caros} produtos custando mais de R$1000')
print(f'O produto mais barato foi {nome_barato} custando R$ {mais_barato:.2f}')
