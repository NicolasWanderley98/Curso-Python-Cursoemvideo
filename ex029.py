velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade >80:
    print('Multado! Você exedeu o limite permitido que é de 80Km/h')
    multa=(velocidade-80)*7
    print('Sua multa é de R$ {:.2f}'.format(multa))
print('Tenha um Bom dia! Dirija com segurança!')
