from django.urls import path
from me_poupe.views import index, despesa, relatorio, cadastro_despesa, listar_despesas, excluir_despesa, editar_despesa, pesquisar


urlpatterns = [

  path('', index, name='index'),
  path('despesa/', despesa, name='despesa'),
  path('despesa/relatorio/', relatorio, name='relatorio'),
  path('despesa/cadastro/', cadastro_despesa, name='cadastro_despesa'),
  path('despesa/listar/', listar_despesas, name='listar_despesas'),
  path('despesa/excluir/<int:id>/', excluir_despesa, name='excluir_despesa'),
  path('despesa/editar/<int:id>/', editar_despesa, name='editar_despesa'),
  path('despesa/pesquisar/', pesquisar, name='pesquisar'),
]