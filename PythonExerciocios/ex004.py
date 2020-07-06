algo = input('Digite algo: ')

print('Seu tipo primitivo é {}'.format(type(algo)))
print('É um número? {}'.format(algo.isnumeric()))
print('É uma letra? {}'.format(algo.isalpha()))
print('Tem letras e números? {}'.format(algo.isalnum()))
print('Está em maiúsculo? {}'.format(algo.isupper()))
print(('Está em minúsculo? {}'.format(algo.islower())))
