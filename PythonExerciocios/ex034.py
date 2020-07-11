sal = float(input('Digite seu salário R$'))
if sal <= 1250:
    acrescimo = sal + sal * 0.15
    print('Salário com acréscimo de 15% R${:.2f}'.format(acrescimo))
else:
    acrescimo = sal + sal * 0.10
    print('Salário com acrécimo de 10% R${:.2f}'.format(acrescimo))
