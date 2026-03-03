from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Despesa
from django.db.models import Sum
import json



# Create your views here.

def index(request):
    return render(request, "index.html")

def despesa(request):

    despesas = Despesa.objects.all()

    total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0

    total = float(total)

    return render(request, 'despesa.html', {
        'despesas': despesas.order_by('-data'),
        'total': total
    })

def relatorio(request):
    return render(request, "relatorio.html")

def cadastro_despesa(request):
    if request.method == 'POST':
        Despesa.objects.create(
            descricao=request.POST.get('descricao'),
            valor=request.POST.get('valor'),
            data=request.POST.get('data'),
            categoria=request.POST.get('categoria')
        )

    return redirect('listar_despesas')

def listar_despesas(request):

    query = request.GET.get('q')

    if query:
        despesas = Despesa.objects.filter(descricao__icontains=query)
    else:
        despesas = Despesa.objects.all()

    total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0

    return render(request, 'despesa.html', {
        'despesas': despesas.order_by('-data'),
        'total': total
    })

def excluir_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    despesa.delete()
    return redirect('cadastro_despesa')

def editar_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)

    if request.method == 'POST':
        despesa.descricao = request.POST.get('descricao')
        despesa.valor = request.POST.get('valor')
        despesa.data = request.POST.get('data')
        despesa.categoria = request.POST.get('categoria')
        despesa.save()

        return redirect('listar_despesas')

    despesas = Despesa.objects.all()
    total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0

    return render(request, 'despesa.html', {
        'despesas': despesas.order_by('-data'),
        'total': total,
        'despesa': despesa
    })

def pesquisar(request):
    query = request.GET.get('q')

    despesas = Despesa.objects.all()

    if query:
        despesas = despesas.filter(descricao__icontains=query)

    total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0

    return render(request, 'despesa.html', {
        'despesas': despesas.order_by('-data'),
        'total': total
    })

def relatorio(request):
    dados = (
        Despesa.objects
        .values('categoria')
        .annotate(total=Sum('valor'))
        .order_by('categoria')
    )

    categorias = [item['categoria'] for item in dados]
    totais = [float(item['total']) for item in dados]

    return render(request, 'relatorio.html', {
        'categorias': json.dumps(categorias),
        'totais': json.dumps(totais)
    })