from datetime import date
atual = date.today().year
ano = int(input('Qual seu ano de nascimento ?'))
idade = atual - ano
print('O atelta tem {} anos.'.format(idade))
if idade <= 9:
    print('Voçê é Mirim')
elif idade <14:
    print('Voçê é Infantil')
elif idade <=19:
    print('Voçê é Junior')
elif idade <=25:
    print('Voçê é Sênior')
elif idade >25:
    print('Voçê é Master')
