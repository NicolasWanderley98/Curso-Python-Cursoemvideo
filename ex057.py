sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in'MmFf':
    sexo = str(input('Dados inválios, por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

