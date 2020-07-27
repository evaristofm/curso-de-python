sal = float(input('Digite seu salário R$'))
if sal <= 1250:
    acrescimo = sal + sal * 0.15

else:
    acrescimo = sal + sal * 0.10
print('Quem ganhava {:.2f} passa a ganhar R${:.2f} agora'.format(sal, acrescimo))