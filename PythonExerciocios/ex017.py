from math import hypot
co = float(input('Imforme o cateto oposto: '))
ca = float(input('Informe a cateto adjacente: '))
hipo = hypot(co, ca)
print('Hipotenusa igual a {:.2f}'.format(hipo))
