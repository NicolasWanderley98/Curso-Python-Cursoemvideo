from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('vai sé alistar!')
elif idade < 18:
    saldo = 18 - idade
    print('ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('ainda falta {} anos'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Já deveria ter indo há {} anos.'.format(saldo))
    ano = atual - saldo
    print('foi no ano {}'.format(ano))
