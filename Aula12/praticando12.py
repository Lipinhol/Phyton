nome = str(input('Qual é o seu nome?')).title()
if nome == 'Luiz':
    print('Que nome bonito!')
elif nome == 'Everton' or nome == 'Daiane' or nome == 'Caio':
    print('Seu nome é bem popular no Brasil.')
elif nome in ('Ana Claudia Jéssica Juliana'):
    print('Belo nome feminino!')
else:
    print('Seu nome é comum!')
print('Tenha um dia dia {}.'.format(nome.title()))