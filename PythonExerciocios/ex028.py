from time import sleep
from random import randint
guess = randint(0, 5)
print('Estou pensando em um número...')
sleep(1)
num = int(input('Adivinhe qual é [Entre 0 e 5]: '))
if guess == num:
    print('Parabéns!! Você venceu!!')
    print('O número que eu pensei foi {}!'.format(guess))
else:
    print('O computador venceu!!')
    print('O número que eu pensei foi {}!'.format(guess))
print('---FIM---')
