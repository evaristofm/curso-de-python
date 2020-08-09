nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Média: {},  REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Média: {}, RECUPERAÇÃO'.format(media))

else:
    print('Média: {}, APROVADO!'.format(media))
