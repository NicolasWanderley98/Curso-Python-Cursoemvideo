def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


print('Controle de terrenos')
print('-' * 30)
l = float(input('Largura (M): '))
c = float(input('Comprimento (M): '))
area(l,c)
