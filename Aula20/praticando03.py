def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    print(f'Recebi os valores {num} e são ao todo {len(num)} números.')


contador(2, 1, 7)

contador(8, 0)

contador(4, 4, 7, 6, 2)