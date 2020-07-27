km = int(input('Qual a distância da viagem em (km): '))
if km <= 200:
    print('Preço cobrado por km R$0,50')
    print('Total da viagem R${:.2f}'.format(km * 0.50))
else:
    print('Preço cobrado por km R$0,45')
    print('Total da viagem R${}'.format(km * 0.45))
