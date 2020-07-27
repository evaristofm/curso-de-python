velo = float(input('Informe a velocidade: '))
if velo > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velo - 80) * 7
    print('O total da multa é de R${:.2f}'.format(multa))
else:
    print('Dentro da velocidade permitida!')
