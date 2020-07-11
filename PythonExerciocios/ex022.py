nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())
novo_name = nome.split()
print('Tamanho do seu nome sem espaços:', len(''.join(novo_name)))
print('Seu primeiro nome {} tem um total de {} letras.'.format(novo_name[0], len(novo_name[0])))

