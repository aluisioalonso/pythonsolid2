def notas(*num):
    """
    -> funcao para analisar notas e situacoes de varios alunos
    :param num: uma ou mais notas de alunos(aceitas varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre os alunos

    """

    nota = {}
    nota['total'] = len(num)
    nota['maior'] = max(num)
    nota['menor'] = min(num)
    nota['media'] = sum(num) / len(num)

    return nota



resp = notas(5.5,6,7,8,9)
print(resp)