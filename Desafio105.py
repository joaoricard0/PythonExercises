# def notas(*nota, sit=False):
    # """
    # -> Função para analisar notas e situações de vários alunos.
    # :param nota: uma ou mais notas dos alunos (aceita várias).
    # :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    # :return: dicionário com várias informações sobre a situação da turma.
    # """
#     dicio = {}
#     soma = maior = menor = media = cont = 0
#     for i in nota:
#         if cont == 0:
#             maior = menor = i
#         else:
#             if i > maior:
#                 maior = i
#             if i < menor:
#                 menor = i
#         cont += 1
#         soma += i
#     media = soma / cont
#     dicio['total'] = cont
#     dicio['maior'] = maior
#     dicio['menor'] = menor
#     dicio['média'] = media
#     if sit == True:
#         if media >= 9.5:
#             dicio['situação'] = 'BOA'
#         else:
#             dicio['situação'] = 'MÁ'
#     return dicio
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 14:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 10:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Má'
    return r

resp = notas(12,13,12,13,17,8,10,7,3,7,12,sit=True)
print(resp)
help(notas)
