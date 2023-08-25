from django.shortcuts import render, redirect
from .forms import ClienteForm, ClientePFForm, ClientePJForm
from .models import Cliente


def clientes_home(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'clientes/pages/clientes.html', context)
