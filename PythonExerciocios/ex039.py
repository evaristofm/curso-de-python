data = int(input('Informe sua data de nascimento: '))
idade = 2020 - data
if idade < 18:
    print('Idade: {} anos! Você ainda não está na idade de se alistar! Ainda faltam {} anos!'.format(idade, 18 - idade))
elif idade == 18:
    print('Está na idade do alistamento!')
else:
    print('Idade: {} anos! Já passou do prazo do alistamento! Passou {} anos do alistamento!'.format(idade, idade - 18))
