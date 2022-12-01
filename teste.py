import random


def geranumber(apos, num, em):
    arr = []
    for i in range(1, apos+1):
        numeros = random.sample(range(1, em+1), num)
        numeros.sort()
        arr.append(numeros)

    return arr


if __name__ == '__main__':
    # Numero de apostas que quero fazer
    apos = 4
    # Quantos numeros eu quero escolher
    num = 6
    # De 1 a qual numero quero gerar minha aposta
    em = 60

    for num in geranumber(apos, num, em):
        print(num)


# apostas = [{'loteria': 'lotomania', 'nome': 'Lotomania', 'concurso': 2359, 'data': '31/08/2022', 'local': 'ESPAÇODASORTE em SÃOPAULO,SP', 'dezenas': ['05', '09', '11', '14', '16', '21', '34', '47', '53', '61', '64', '68', '69', '75', '76', '86', '95', '96', '98', '99'], 'premiacoes': [{'acertos': '20 Pontos', 'vencedores': 1, 'premio': '1.288.040,49'}, {'acertos': '19 Pontos', 'vencedores': 2, 'premio': '98.638,31'}, {'acertos': '18 Pontos', 'vencedores': 51, 'premio': '2.417,61'}, {'acertos': '17 Pontos', 'vencedores': 451, 'premio': '273,38'}, {'acertos': '16 Pontos', 'vencedores': 2707, 'premio': '45,54'}, {'acertos': '15 Pontos', 'vencedores': 12151, 'premio': '10,14'}, {'acertos': '0 Pontos', 'vencedores': 0, 'premio': '0,00'}], 'estadosPremiados': [{'nome': 'Pará', 'uf': 'PA', 'vencedores': '1', 'latitude': '-1.9981271', 'longitude': '-54.9306152', 'cidades': [{'cidade': 'Ananindeua', 'vencedores': '1', 'latitude': '-1.3650671', 'longitude': '-48.3746372'}]}], 'acumulou': False, 'acumuladaProxConcurso': '', 'dataProxConcurso': '', 'proxConcurso': 2360, 'timeCoracao': None, 'mesSorte': None}, {'loteria': 'lotomania', 'nome': 'Lotomania', 'concurso': 2354, 'data': '19/08/2022', 'local': 'ESPAÇODASORTE em SÃOPAULO,SP', 'dezenas': ['09', '13', '21', '28', '29', '34', '40', '41', '43', '50', '59', '67', '70', '74', '82', '85', '88', '90', '95', '98'], 'premiacoes': [{'acertos': '20 Pontos', 'vencedores': 0, 'premio': '-'},
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {'acertos': '19 Pontos', 'vencedores': 6, 'premio': '44.717,49'}, {'acertos': '18 Pontos', 'vencedores': 60, 'premio': '2.794,85'}, {'acertos': '17 Pontos', 'vencedores': 623, 'premio': '269,16'}, {'acertos': '16 Pontos', 'vencedores': 3928, 'premio': '42,69'}, {'acertos': '15 Pontos', 'vencedores': 17141, 'premio': '9,78'}, {'acertos': '0 Pontos', 'vencedores': 1, 'premio': '134.152,48'}], 'estadosPremiados': [], 'acumulou': True, 'acumuladaProxConcurso': '', 'dataProxConcurso': '', 'proxConcurso': 2355, 'timeCoracao': None, 'mesSorte': None}, {'loteria': 'lotomania', 'nome': 'Lotomania', 'concurso': 2355, 'data': '22/08/2022', 'local': 'ESPAÇODASORTE em SÃOPAULO,SP', 'dezenas': ['01', '05', '11', '16', '19', '35', '38', '41', '43', '46', '47', '54', '63', '65', '67', '72', '75', '89', '93', '94'], 'premiacoes': [{'acertos': '20 Pontos', 'vencedores': 0, 'premio': '-'}, {'acertos': '19 Pontos', 'vencedores': 4, 'premio': '66.388,37'}, {'acertos': '18 Pontos', 'vencedores': 72, 'premio': '2.305,15'}, {'acertos': '17 Pontos', 'vencedores': 751, 'premio': '220,99'}, {'acertos': '16 Pontos', 'vencedores': 4492, 'premio': '36,94'}, {'acertos': '15 Pontos', 'vencedores': 19183, 'premio': '8,65'}, {'acertos': '0 Pontos', 'vencedores': 0, 'premio': '0,00'}], 'estadosPremiados': [], 'acumulou': True, 'acumuladaProxConcurso': '', 'dataProxConcurso': '', 'proxConcurso': 2356, 'timeCoracao': None, 'mesSorte': None}]

# apostas_n = []

# for i in range(0, len(apostas)):
#     apostas_n.append({x: y for x, y in apostas[i].items(
#     ) if x == 'concurso' or x == 'data' or x == 'dezenas' or x == 'premiacoes'})

# lista = {'1': 'abs', '2': 'agora', '3': 'autos'}
# lista['4'] = 'agora'
# print(lista)


# mesa = [1, 2, 8, 4, 5, 55, 56, 100, 2]

# n_mesa = [str(x) if len(str(x)) == 2 else str(
#     f"0{x}") if len(str(x)) == 1 else "00" for x in mesa]


# print(n_mesa)
