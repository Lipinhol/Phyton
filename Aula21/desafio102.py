def fatorial(num=1, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    Função criada por Luiz Filipe.
    '''
    f = 1
    for c in range(num, 0, -1):
        if show: 
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f

n = int(input('Digite um número: '))
help(fatorial)
print(fatorial(n, show=True))
