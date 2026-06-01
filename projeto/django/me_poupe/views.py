from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Despesa
from django.db.models import Sum
import json

# NOTA: O decorator @csrf_exempt é necessário temporariamente para permitir que o React 
# faça requisições POST/PUT/DELETE sem travar no erro de segurança CSRF do Django.

def listar_e_somar_despesas(query_set):
    """Função auxiliar para transformar o QuerySet do Django em uma lista de dicionários python"""
    lista = []
    for d in query_set:
        lista.append({
            'id': d.id,
            'descricao': d.descricao,
            'valor': float(d.valor),
            'data': d.data.strftime('%Y-%m-%d') if d.data else None,
            'categoria': d.categoria
        })
    return lista


def despesa(request):
    """Retorna todas as despesas e o total geral em formato JSON"""
    despesas = Despesa.objects.all().order_by('-data')
    total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0

    dados = {
        'despesas': listar_e_somar_despesas(despesas),
        'total': float(total)
    }
    return JsonResponse(dados)


@csrf_exempt
def cadastro_despesa(request):
    """Recebe um JSON do React e cria uma nova despesa"""
    if request.method == 'POST':
        # O React envia os dados dentro do body como string JSON, precisamos decodificar:
        data = json.loads(request.body)
        
        nova_despesa = Despesa.objects.create(
            descricao=data.get('descricao'),
            valor=data.get('valor'),
            data=data.get('data'),
            categoria=data.get('categoria')
        )
        
        return JsonResponse({'mensagem': 'Despesa cadastrada com sucesso!', 'id': nova_despesa.id}, status=201)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


def pesquisar(request):
    """Filtra despesas com base no termo 'q' enviado na URL pelo React"""
    query = request.GET.get('q', '')
    despesas = Despesa.objects.all()

    if query:
        despesas = despesas.filter(descricao__icontains=query)

    total = despesas.aggregate(Sum('valor'))['valor__sum'] or 0
    despesas = despesas.order_by('-data')

    dados = {
        'despesas': listar_e_somar_despesas(despesas),
        'total': float(total)
    }
    return JsonResponse(dados)


@csrf_exempt
def excluir_despesa(request, id):
    """Exclui uma despesa do banco de dados"""
    if request.method == 'DELETE':
        despesa_obj = get_object_or_404(Despesa, id=id)
        despesa_obj.delete()
        return JsonResponse({'mensagem': 'Despesa excluída com sucesso!'}, status=200)
    
    return JsonResponse({'erro': 'Método não permitido'}, status=405)


@csrf_exempt
def editar_despesa(request, id):
    """Atualiza os dados de uma despesa existente"""
    despesa_obj = get_object_or_404(Despesa, id=id)

    if request.method == 'PUT' or request.method == 'POST':
        data = json.loads(request.body)
        
        despesa_obj.descricao = data.get('descricao', despesa_obj.descricao)
        despesa_obj.valor = data.get('valor', despesa_obj.valor)
        despesa_obj.data = data.get('data', despesa_obj.data)
        despesa_obj.categoria = data.get('categoria', despesa_obj.categoria)
        despesa_obj.save()

        return JsonResponse({'mensagem': 'Despesa atualizada com sucesso!'}, status=200)

    # Se for um GET, retorna os dados da despesa específica para preencher o formulário no React
    dados_despesa = {
        'id': despesa_obj.id,
        'descricao': despesa_obj.descricao,
        'valor': float(despesa_obj.valor),
        'data': despesa_obj.data.strftime('%Y-%m-%d') if despesa_obj.data else None,
        'categoria': despesa_obj.categoria
    }
    return JsonResponse(dados_despesa)


def relatorio(request):
    """Retorna os dados agrupados por categoria perfeitos para gerar gráficos no React"""
    dados_agrupados = (
        Despesa.objects
        .values('categoria')
        .annotate(total=Sum('valor'))
        .order_by('categoria')
    )

    resultado = []
    for item in dados_agrupados:
        resultado.append({
            'categoria': item['categoria'],
            'total': float(item['total'])
        })

    # Retorna direto a lista de objetos para o React mapear facilmente
    return JsonResponse(resultado, safe=False)