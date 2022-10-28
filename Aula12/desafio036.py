#Informações necessárias para o cálcul de financiamento.
salario = float(input('Digite seu salário: R$'))
valor_casa = float(input('Diga o valor da casa pretendido: R$'))
tempo = int(input('Em quantos anos você quer pagar o emprestimo? '))

#Calculos baseados nas infomrções dadas pelo o usuario.
calculo_parcela = valor_casa / (tempo * 12)
limite_conforme_salario = (salario * 30) / 100

if calculo_parcela > limite_conforme_salario:
    print('Infelizmente não atingiu os requisitos minimos, tente aumentar o tempo de financiamento do imovel.')
if limite_conforme_salario >= calculo_parcela:
    print('Crédito de financiamneto de R${:.2F} aprovado com parcelas de R${:.2F} ao mês a serem quitadas em {} anos.'.format(valor_casa, calculo_parcela, tempo))
