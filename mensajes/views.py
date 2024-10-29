from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def mensajes_list(request):
    mensajes = Mensaje.objects.all()

    context = {
        'mensajes': mensajes,
        'titulo': 'Principal'
    }

    return render(request, 'mensajes/mensajes_list.html', context)

def mensajes_create(request):
    form = mensajesModelForm()
    if request.method == 'POST':
        form = mensajesModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(mensajes_list)
    context = {
        'form': form,
        'titulo': 'Crear Mensaje'
    }

    return render(request, 'mensajes/mensajes_create.html', context)

def mensajes_delete(request, pk):
    Mensaje.objects.get(pk=pk).delete()
    return redirect(mensajes_list)
