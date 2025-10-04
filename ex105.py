def notas(*n, sit=False):
    """
    Função para analisar notas e situação de varios alunos
    :param n: uma ou mais notas do aluno (aceita varias)
    :param sit:valor opcional, indica se deve ou não aadicionar a situação
    :return:dicionario com varias informaçes sobre a turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'Razoavel'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5,2.5,1.5, sit=True)
print(resp)
help(notas)