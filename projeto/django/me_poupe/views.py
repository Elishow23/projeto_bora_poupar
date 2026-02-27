from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def despesa(request):
    return render(request, "despesa.html")

def relatorio(request):
    return render(request, "relatorio.html")

def cadastroDespesa(request):
    return render(request, "cadastroDespesa.html")