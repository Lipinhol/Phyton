n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media > 6.0:
    print ('PARABÉNS, sua média é {:.2f}. Você está APROVADO!'.format(media))
elif media > 4.0  and media < 6.0:
    print('Você não atingiu a média, sua nota foi {:.2f}. Você deverá realizar a recuperação!'.format(media))
elif media < 4.0:
    print('Sua média é {:.2f}. Você está REPROVADO, estude mais no próximo semestre!'.format(media))