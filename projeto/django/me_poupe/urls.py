from django.urls import path
from me_poupe.views import index, despesa, relatorio, cadastroDespesa


urlpatterns = [

  path('', index, name='index'),
  path('despesa/', despesa, name='despesa'),
  path('relatorio/', relatorio, name='relatorio'),
  path('cadastroDespesa/', cadastroDespesa, name='cadastroDespesa'),

]