from django.urls import path
from me_poupe.views import index, despesa, relatorio, cadastro_despesa, listar_despesas, excluir_despesa


urlpatterns = [

  path('', index, name='index'),
  path('despesa/', despesa, name='despesa'),
  path('relatorio/', relatorio, name='relatorio'),
  path('despesa/cadastro/', cadastro_despesa, name='cadastro_despesa'),
  path('despesa/listar/', listar_despesas, name='listar_despesas'),
  path('despesa/excluir/<int:id>/', excluir_despesa, name='excluir_despesa'),
]