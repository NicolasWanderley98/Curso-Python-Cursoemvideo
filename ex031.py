distancia=float(input('Qual a distância da sua viagem ? '))
if distancia <= 200:
    preço= distancia * 0.50
else:
    preço=distancia* 0.40
print('O preço da sua passagem será de R${:.2f}'.format(preço))