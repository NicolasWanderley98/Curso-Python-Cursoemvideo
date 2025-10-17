def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um numero inteiro valido .')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um numero valido .')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor digitado inteiro foi {n1} e o valor real foi {n2}')