nome = input('Digite seu nome completo: ').strip().title()
print('Seu nome é: {}'.format(nome))
separa = nome.split()
print('Seu primeiro nome é: {}'.format(separa[0]))
print('Seu ultimo nome é {}'.format(separa[len(separa)-1]))