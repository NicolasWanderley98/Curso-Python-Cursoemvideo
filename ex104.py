def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro! Digite um numero inteiro.')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você Acabou de digitar o número:  {n}')
