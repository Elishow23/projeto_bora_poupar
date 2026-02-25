from django.urls import path

from me_poupe.views import index


urlpatterns = [

  path('', index, name='index'),

]