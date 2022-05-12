from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Cliente
from .forms import ClienteForm, UserRegistrationForm

# Create your views here.
@login_required

def index(request):

    listado = Cliente.objects.all()
    
    return render(request, 'aplicacion/index.html', {'context':listado})

def formulario(request):
    return render(request,'aplicacion/formulario.html')

def create(request):
    form = ClienteForm(request.POST)
    if request.method == 'POST':
    # print(request.POST)
        

        if form.is_valid():
            cliente = Cliente()
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.edad = form.cleaned_data['edad']
            cliente.email = form.cleaned_data['email']
            cliente.fecha_contratacion = form.cleaned_data['fecha_contratacion']    
            cliente.save()

        else:
            print('Invalido')
        
        return redirect('/aplicacion')
    
    return render(request, 'aplicacion/create.html', {'form': form}) 

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('login')
    else:
        form = UserRegistrationForm()

        context = {'form':form}
        
    return render(request, 'aplicacion/register.html', context)