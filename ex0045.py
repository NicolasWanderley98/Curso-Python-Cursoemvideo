from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!!!')
print('-=' * 11)
print('Computador jogou {}'.format (itens [computador]))
print('Jogador jogou {}'.format (itens [jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print ('Empate')
    elif jogador == 1:
        print ('Jogador Vence')
    elif jogador == 2:
        print ('Computador vence')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print ('Computador vence')
    elif jogador == 1:
        print ('Empate')
    elif jogador == 2:
        print ('Jogador vence')
    else:
        print('Jogada inválida!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print ('Computador vence')
    elif jogador == 2:
        print ('empate')
    else:
        print('Jogada inválida!')
