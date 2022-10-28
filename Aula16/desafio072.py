contagem = ['ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO',
            'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE',
            'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE',
            'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO',
            'DEZENOVE', 'VINTE']

while True:           
    while True:
        escolha = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= escolha <= 20:
            break
        print('Digite um número entre 0 e 20: ')
    print(f'Você digitou o número {contagem[escolha]}.')
    resp = str(input('Você deseja continuar? [S/N]')).upper().strip()
    if resp == 'N':
        break
    

