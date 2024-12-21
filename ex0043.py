peso = float(input('Qual é seu peso? (KG)' ))
altura = float(input('Qual é sua altura? (M)' ))
imc = peso / (altura ** 2)
print(' O IMC dessa pessoa é de {:.1f} '.format (imc))
if imc < 18.1:
    print('Seu peso está abaixo do normal')
elif imc >=18.5 and imc <25:
    print('Seu peso está otimo')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')

