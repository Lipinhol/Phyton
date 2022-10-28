lista = list()

while True:
    nome =  str(input('Qual o nome do aluno? '))
    nota1 = float(input('Sua primeira nota: '))
    nota2 = float(input('E sua segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja cadastrar mais alunos? [S/N]'))
    if continuar in 'Nn':
        break
print('=-' * 30)
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} sao {lista[opc][1]}')

print('<<<   VOLTE SEMPRE!   >>>')