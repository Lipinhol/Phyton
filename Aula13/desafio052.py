num = int(input('Digite um número: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total = total + 1
    else:
        print('\033[031m', end='')
    print('{}'.format(c), end='')
print('\n\033[mO numero {} é divisivel {} vezes.'. format(num, total))
if total == 2:
    print('E por isso ele e PRIMO!')
else:
    print('E por isso ele NÃO E PRIMO!')

