opção = 0

n1 = int(input('Digite o 1º numero: '))
n2 = int (input('Digite o 2º numero: '))

while opção != 5:
    
    print('''
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')
    opção = int(input('\nOs numeros digitados foram {} e {}. Escolha no menu acima qual operação deseja relizar: '.format(n1, n2)))
    if opção == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, soma))

    elif opção == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, multiplicar))

    elif opção == 3:
        if n1 == n2:
            print('Os numeros {} e {} tem o mesmo valor.'.format(n1, n2))            
        elif n1 > n2:            
            print('Entre {} e {} o maior é {}'.format(n1, n2, n1))
        else:            
            print('Entre {} e {} o maior é {}'.format(n1, n2, n2))

    elif opção == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    
    else:
        print('FINALIZANDO...')
    
print('Fim do programa. Volte sempre!')



