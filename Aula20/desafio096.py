def area(a, b):
    result = a * b
    print(f'A área de um terreno {a}x{b} é {result}m².')


print('-=' * 20)
print('        CONTOLE DE TERRENOS')
print('-=' * 20)  
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
