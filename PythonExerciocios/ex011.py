altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))
area = largura * altura
print('Total da área: {:.2f}'.format(area))
print('Serão necessários {:.2f} litros de tinta.'.format(area / 2))