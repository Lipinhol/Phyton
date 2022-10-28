classificacao = ('Palmeiras', 'Corinthians', 'Internacional',
                'Atletico Mg', 'Fluminense', 'Athletico PR',
                'Sao Paulo', 'Santos', 'Flamengo', 'Botafogo',
                'Bragantino', 'Goias', 'Cuiaba', 'Coritiba',
                'America MG', 'Avai', 'Ceara', 'Atletico GO',
                'Juventude', 'Fortaleza')
print('-=' * 15)
print(f'Os cinco primerios colocados são: {classificacao[0:5]}')
print('-=' * 15)
print(f'Os quatro ultimos colocados são: {classificacao[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabetica são: {sorted(classificacao)}')
print('-=' * 15)
print(f'O Santos está na posição {classificacao.index("Santos")+1}ª')
