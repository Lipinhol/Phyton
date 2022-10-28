palavras = ('leite', 'mouse', 'caneta', 'calular', 'controle', 'teclado', 'cd',
            'monitor', 'video game', 'fone de ouvido', 'xicara', 'massageador')

for p in palavras:
    print(f'\nNa palavra {p.upper()} contêm as vogais: ', end='') 
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')