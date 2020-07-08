from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo:'))
print('O seno de {} corresponde a {:.2f}'.format(angulo, sin(radians(angulo))))
print('O cosseno de {} corresponde a {:.2f}'.format(angulo, cos(radians(angulo))))
print('A tangente de {} corresponde a {:.2f}'.format(angulo, tan(radians(angulo))))
