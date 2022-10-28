frase = input('Escreva uma frase: ').upper().strip()

print('A sua frase possui {} letras A.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A do seu nome aparece na posição {}'.format(frase.rfind('A')+1))