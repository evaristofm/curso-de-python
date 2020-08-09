emprestimo = float(input("Valor da casa R$ "))
salario = float(input("Seu salário R$ "))
parcela = int(input('Parcela: '))

mensalidade = emprestimo / parcela
limite = (salario * 0.30)
if mensalidade > limite:
    print("Empréstimo não aprovado! limite de 30% do salário excedido!")
else:
    print("Valor da mensalidade vai ser {}x de R${:.2f}".format(parcela, mensalidade))
