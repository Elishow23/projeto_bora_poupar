from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Despesa
from django.shortcuts import redirect
from django.db.models import Sum


# Create your views here.

def index(request):
    return render(request, "index.html")

def despesa(request):
    return render(request, "despesa.html")

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