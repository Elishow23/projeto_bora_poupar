from django.urls import path
from me_poupe.views import index, despesa, relatorio, cadastroDespesa, categoria


urlpatterns = [

  path('', index, name='index'),
  path('despesa/', despesa, name='despesa'),
  path('relatorio/', relatorio, name='relatorio'),
  path('despesa/cadastro/', cadastroDespesa, name='cadastroDespesa'),
  path('despesa/categoria/', categoria, name='categoria'),

]