from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,'aplicacion/index.html')

def formulario(request):
    return render(request,'aplicacion/formulario.html')

