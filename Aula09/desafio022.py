nome = input('Digite seu nome: ').strip()

print('Lendo seu nome...\n')
print('Seu nome com todas letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome com todas as letras maiúsculas é {}'.format(nome.lower()))
print('Seu nome possui no total {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome contém um total de {} letras'.format(len(separa[0])))


