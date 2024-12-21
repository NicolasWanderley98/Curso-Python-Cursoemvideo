from random import randint
pc = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente advinhar...')
print('-=-' * 20)
play = int(input('Em que núnemo eu penseu ?'))
if play == pc:
    print('Parabéns! Você acertou {}'.format(pc))
else:
    print('Eu ganhei pensei no número {} e não no {}'.format(pc,play))