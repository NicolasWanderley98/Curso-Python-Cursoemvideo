larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg,alt,area))
tinta = area / 2
print ('para pintar essa parede, você precisa de {}L de tinta.'.format(tinta))
