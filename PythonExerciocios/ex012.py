preco = float(input('Informe o preço do produto? R$'))
desconto = preco - (preco * 0.05)
print('Produto com 5% de desconto: R${:.2f} reais'.format(desconto))