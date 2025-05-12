print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end='')
        termo = termo + razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você que mostrar a mais ? '))
print('Progresão finalizada com {} termos mostrados'.format(total))
