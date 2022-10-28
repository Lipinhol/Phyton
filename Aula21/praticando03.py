def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de tres valores.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    Função criada por Luiz Filipe.
    """
    s = a + b +c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')