cont = ('Zero', 'Um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
resp = 'S'
while resp == 'S':
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        print(f'Você digitou o número {cont[núm]}')
        resp = input(str('Deseja executar outra vez? [S/N]')).upper().strip()[0]
    else:
     print('tente novamente. ', end='')