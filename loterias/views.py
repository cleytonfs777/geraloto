import json
from dataclasses import fields
from datetime import date, datetime

import requests
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .lotoapi import conc_result2, sync_base
from .models import Apostas


def home(request):
    return render(request, 'home.html')


def cadastrar_aposta(request):
    status = request.GET.get('status')
    return render(request, 'cadastrar_aposta.html', {'status': status})


def trata_aposta(request):
    concurso = request.POST.get('concurso')
    num_selected = request.POST.get('num_selected')
    data = request.POST.get('data')
    teimosinha = request.POST.get('teimosinha')
    selteimosinha = request.POST.get('selteimosinha')
    cont_aposta = []
    print(f"concurso: {concurso}")
    print(f"num_selected: {num_selected}")
    print(f"data: {data}")
    print(f"teimosinha: {type(teimosinha)}")
    print(f"selteimosinha: {type(selteimosinha)}")

    if (teimosinha == 'on'):
        if selteimosinha == '2':
            cont_aposta = [int(concurso)+x for x in range(0, 2)]

        elif selteimosinha == '4':
            cont_aposta = [int(concurso)+x for x in range(0, 4)]

        elif selteimosinha == '8':
            cont_aposta = [int(concurso)+x for x in range(0, 8)]
    else:
        cont_aposta.append(int(concurso))

    for n_concurso in cont_aposta:

        aposta = Apostas.objects.filter(
            concurso=n_concurso, num_selected=num_selected)
        if (aposta):
            return redirect('/cadastrar_aposta/?status=2')
        else:
            num_selected2 = json.loads(f"[{num_selected}]")
            if (len(num_selected2) < 50):
                return redirect('/cadastrar_aposta/?status=3')
            else:
                aposta = Apostas(concurso=n_concurso,
                                 num_selected=num_selected, data=data)
                aposta.save()
    return redirect('/cadastrar_aposta/?status=1')


def ver_apostas(request):
    conf = []
    concs = []
    results = []
    apostas = serializers.serialize("json", Apostas.objects.all())
    apostas = eval(apostas)
    for aposta in apostas:
        aposta['fields']['pk'] = aposta['pk']
        conf.append(aposta['fields'])
    for i in range(0, len(conf)):
        conf[i]['num_selected'] = eval(f"[{conf[i]['num_selected']}]")
        conf[i]['num_selected'] = [str(x) if len(str(x)) == 2 else f"0{x}" if len(
            str(x)) == 1 else "00" for x in conf[i]['num_selected']]

        concs.append(conf[i]['concurso'])

    concs = sorted(set(concs))
    for conc in concs:
        conc = int(conc)
        if len(conc_result2(conc)) == 0:
            results.append({"concurso": f"{conc}", "resultado": "aguardando"})
        else:
            results.append(conc_result2(conc))

    print(results)
    print(len(results))

    results_n = []
    for i in range(0, len(results)):
        if results[i].__contains__("resultado"):
            results_n.append(results[i])
        else:
            results_n.append({x: y for x, y in results[i].items(
            ) if x == 'concurso' or x == 'data' or x == 'dezenas' or x == 'premiacoes' or x == 'pk'})

    for i in range(0, len(conf)):
        for rst in results_n:
            if str(conf[i]['concurso']) == str(rst['concurso']):
                if rst.__contains__("resultado"):
                    rst['pk'] = conf[i]['pk']
                    rst['num_selected'] = conf[i]['num_selected']
                    conf[i] = rst
                else:
                    conf[i]['resultados'] = rst['dezenas']
                    conf[i]['premiacoes'] = rst['premiacoes']

        if not conf[i].__contains__("resultado"):
            conf[i]['acertos_n'] = len(
                [x for x in conf[i]['num_selected'] if x in conf[i]['resultados']])
    status = request.GET.get('status')

    return render(request, 'ver_apostas.html', {'conf': conf, 'status': status})


def excluir_apostas(request, id):
    apostas = Apostas.objects.get(id=id).delete()
    return redirect('/ver_apostas/?status=1')


def teste(request):
    lli = ['2345', '2359', '2363', '2355', '2354']
    teste = []
    for ll in lli:
        teste.append(conc_result2(ll))
    return render(request, 'teste.html', {'teste': teste})


def edita_apostas(request, id):
    apostas = serializers.serialize("json", Apostas.objects.filter(id=id))
    apostas = eval(apostas)[0]
    apostas['fields']['num_selected_2'] = eval(
        f"[{apostas['fields']['num_selected']}]")
    apostas['tamanho'] = len(apostas['fields']['num_selected_2'])
    # for i in range(0, len(apostas)):
    #     apostas[i]['bolinhas'] = eval(f"[{apostas[i].num_selected}]")
    return render(request, 'edita_apostas.html', {'apostas': apostas, 'edita': True, 'range': range(1, 101)})


def salva_apostas(request, id):
    apostas = Apostas.objects.get(id=id)

    if (request.POST.get('concurso')) != (apostas.concurso):
        apostas.concurso = request.POST.get('concurso')

    if (request.POST.get('num_selected')) != (apostas.num_selected):
        apostas.num_selected = request.POST.get('num_selected')

    if (request.POST.get('data')) != (apostas.data.strftime('%Y-%m-%d')):
        apostas.data = request.POST.get('data')

    apostas.save()

    return redirect(f'/ver_apostas/?status=2')


def sync(request):
    sync_base()
    return redirect(f'/ver_apostas/?status=4')


def estrategias(request):
    return render(request, 'estrategias.html')
