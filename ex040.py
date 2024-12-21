primeira = float(input('Primeira nota: '))
segunda = float(input('Segunda nota:'))
média = (primeira + segunda ) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(primeira,segunda,média))
if média >=5 and média <7:
    print('Recuperação')
elif média <5:
    print('Reprovado')
elif média >=7:
    print('Aprovado')
