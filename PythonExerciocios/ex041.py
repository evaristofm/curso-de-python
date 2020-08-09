ano = int(input("Ano de nascimento: "))
if ano <= 9:
    print('Categoria: MIRIM!')
elif ano > 9 and ano <= 14:
    print('Categoria: INFATIL')
elif ano > 14 and ano <= 19:
    print('Categoria: JUNIOR')
elif ano == 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')