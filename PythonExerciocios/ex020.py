from random import shuffle
a1 = str(input('Nome do 1ª aluno: '))
a2 = str(input('Nome do 2ª aluno: '))
a3 = str(input('Nome do 3ª aluno: '))
a4 = str(input('Nome do 4ª aluno: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print('A ordem de apresentação será')
print(alunos)

