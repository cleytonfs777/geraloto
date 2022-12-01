import json
import os
import random

import requests

# https://loteriascaixa-api.herokuapp.com/api/lotomania/2354 -> Concurso específico
# https://loteriascaixa-api.herokuapp.com/api/lotomania/latest -> Ultimo Consurso
# https://loteriascaixa-api.herokuapp.com/api/lotomania -> Todos os resultados da loteria espefícica


def ult_result():

    dados = requests.get(
        'https://loteriascaixa-api.herokuapp.com/api/lotomania/latest')

    result = dados.json()

    return result


def conc_result(conc):
    try:
        dados = requests.get(
            f'https://loteriascaixa-api.herokuapp.com/api/lotomania/{conc}')

        result = dados.json()
    except:
        result = "Aguardando resultado"

    return result


def conc_result2(conc):
    result = {}
    lista = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lista = os.path.join(lista, 'loterias', 'lotoapi.json')
    with open(lista, 'r') as openfile:
        json_object = json.load(openfile)
        try:
            for num in json_object:
                if num['concurso'] == conc:
                    result = num
        except:
            result = {}
    return result


def aleat_gera():
    for i in range(1, 6):
        numeros = random.sample(range(1, 101), 50)
        numeros.sort()
        return numeros


def sync_base():

    lista = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    lista = os.path.join(lista, 'loterias', 'lotoapi.json')

    dicionario = []
    dicionario.append(ult_result())

    concurso = ult_result()['concurso']

    with open(lista, 'r') as openfile:
        json_object = json.load(openfile)

    for num in json_object:
        if num['concurso'] == concurso:
            print("Base atualizada...")
            return

    t_conc = []
    initi = json_object[-1]['concurso']
    while initi != concurso:
        t_conc.append(initi+1)
        initi += 1

    for resst in t_conc:
        json_object.append(conc_result(resst))

    with open(lista, "w") as outfile:
        json_object2 = json.dumps(json_object, indent=4, ensure_ascii=False)
        outfile.write(json_object2)


if __name__ == '__main__':
    # print(aleat_gera())
    # sync_base()
    print(conc_result2(2363))
