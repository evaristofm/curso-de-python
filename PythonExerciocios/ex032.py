ano = input('Digite o ano: ')
bissexto = int(ano[2:]) / 4
if type(bissexto) == float:
    print('Não é bissexto!!')
else:
    print('É bissexto!!')
