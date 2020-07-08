from math import sqrt
import emoji
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))


print(emoji.emojize("Olá, Mundo :alien:", use_aliases=True))
print(emoji.emojize('Python is :cry:', use_aliases=True))