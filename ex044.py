print('{:=^40}'.format(' Lojas Nick '))
preço = float(input('Preço das compras : R$'))
print('''Formas de Pagamento
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x Cartão
[ 4 ] 3x Cartão ou mais''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3 :
    total = preço
    parcela = total / 2
    print ('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print ('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc, parcela))
else:
    total = preço
    print('não existe essa opção, tente novamente')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format (preço, total))
