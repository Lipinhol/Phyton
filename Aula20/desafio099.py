from time import sleep

def maior(* num):
    cont = 0
    maior = 0
    print('=-' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont = cont + 1
    
    print(f'Foram informados {cont} valores.')
    print(f'O maios valor informado foi {maior}.')

maior(1,5,6,7,8)
maior(9,2,3,4,5,0,9,11,19,14,5)
maior(0)
maior()
