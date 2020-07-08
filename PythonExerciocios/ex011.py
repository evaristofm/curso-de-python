altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = largura * altura
print('Total da área: {:.3f}m²'.format(area))
print('Serão necessários {:.4f} litros de tinta.'.format(area / 2))
