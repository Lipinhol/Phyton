

def voto(num):
    from datetime import date
    atual = date.today().year
    idade = atual - num
    print(idade)
    if idade < 16:
        return f'Com {idade} anos NÃO VOTA.'
    elif 16 <= idade <= 17 or idade > 70:
        return f'Com {idade} anos o voto é OPCIONAL.'
    else:
        return f'Com {idade} anos o voioto é OBRIGATÓRIO.' 

nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))