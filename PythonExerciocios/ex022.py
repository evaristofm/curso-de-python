nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
novo_name = nome.split()
print('Tamanho do seu nome sem espaços:', len(''.join(novo_name)))
print('Seu primeiro nome {} tem um total de {} letras.'.format(novo_name[0], len(novo_name[0])))

