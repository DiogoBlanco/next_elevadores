from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClientePFForm, ClientePJForm, ClienteForm
from .models import Cliente, ClientePF, ClientePJ


def clientes_home(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'clientes/pages/clientes.html', context)


def criar_cliente_cpf(request):
    if request.method == 'POST':
        form = ClientePFForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
    else:
        form = ClientePFForm()
    return render(request, 'clientes/pages/criar_cliente_cpf.html',
                  context={'form': form})


def criar_cliente_cnpj(request):
    if request.method == 'POST':
        form = ClientePJForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clientes')
    else:
        form = ClientePJForm()
    return render(request, 'clientes/pages/criar_cliente_cnpj.html',
                  context={'form': form})


def detalhes_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    context = {
        'cliente': cliente
    }
    return render(request, 'clientes/pages/detalhes_cliente.html', context)


def atualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    form = ClientePJForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('/clientes/detalhes_cliente' + '/' +
                        str(cliente_id) + '/')
    context = {
        'cliente': cliente,
        'form': form
    }
    return render(request, 'clientes/pages/atualizar_cliente.html', context)


def apagar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/clientes')
    context = {
        'cliente': cliente
    }
    return render(request, 'clientes/pages/apagar_cliente.html', context)
