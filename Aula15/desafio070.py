total = 0
mais_1000 = 0
mais_barato = 0

while True:
    nome = str(input('Nome do produto: ')).title().strip()
    valor = float(input('Valor do produto: R$'))
    total = total + valor
    mais_barato = valor

    if valor < mais_barato:
        mais_barato = valor

    if valor > 1000:
        mais_1000 = mais_1000 + 1

    mais_produto = ' '
    while mais_produto not in 'SN':
        mais_produto = str(input('Deseja informar mais produtos? [S/N]')).upper()[0]
    if mais_produto == 'N':
        break

print(f'O total gasto foi R${total}, há {mais_1000} prdutos maior que R$1000.00 e o mais barato da lista é {mais_barato}')