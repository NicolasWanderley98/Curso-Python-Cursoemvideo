def aumentar(preço=0, taxa=0,formato=False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)

def diminuir(preço=0, taxa=0,formato=False):
    res = preço - (preço * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preço=0,formato=False):
    res = preço * 2
    return res if format is False else moeda(res)


def metade(preço=0,formato=False):
    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$ '):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxamais=10, taxamenos=5):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t\t{moeda(preço)}')
    print(f'Dobro do preço: \t\t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço,True)}')
    print(f'{taxamais}% de aumento: \t{aumentar(preço,taxamais,True)}')
    print(f'{taxamenos}% de redução: \t\t{diminuir(preço,taxamenos,True)}')
    print('-' * 40)
