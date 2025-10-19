from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Cadastrar nova pessoa')
    elif resposta == 3:
        cabecalho('Saindo do sistema...')
        break
    else:
        print('Erro, Digite uma opção válida...')
    sleep(2)
