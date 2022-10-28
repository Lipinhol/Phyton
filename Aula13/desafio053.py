frase = str(input('Digite uma frase: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
print('Você digitou a frase: {}.'.format(frase))
inverso = junto[::-1]

print('O inverso de {} é {}.'.format(junto, inverso))

if junto == inverso:
    print('Voce digitou um palindromo!')
else:
    print('Sua frase não é um palindromo.')
