num = int(input('Digite um número inteiro: '))
print('''Escolha uma das base para conversão:
[ 1 ] Converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
