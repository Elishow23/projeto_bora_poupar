from django.urls import path
from me_poupe.views import (
    despesa, 
    relatorio, 
    cadastro_despesa, 
    excluir_despesa, 
    editar_despesa, 
    pesquisar
)

urlpatterns = [
    # Mantivemos os mesmos nomes de caminhos (URLs) que você já tinha:
    path('despesa/', despesa, name='despesa'),
    path('despesa/relatorio/', relatorio, name='relatorio'),
    path('despesa/cadastro/', cadastro_despesa, name='cadastro_despesa'),
    path('despesa/excluir/<int:id>/', excluir_despesa, name='excluir_despesa'),
    path('despesa/editar/<int:id>/', editar_despesa, name='editar_despesa'),
    path('despesa/pesquisar/', pesquisar, name='pesquisar'),
]