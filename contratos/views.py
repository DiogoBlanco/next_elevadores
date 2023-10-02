from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContratoForm
from .models import ContratoAnual


def contratos_home(request):
    contratos = ContratoAnual.objects.all()
    context = {
        'contratos': contratos
    }
    return render(request, 'contratos/pages/contratos.html', context)


def criar_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contratos')
    else:
        form = ContratoForm()
    return render(request, 'contratos/pages/criar_contrato.html',
                  context={'form': form})


def detalhes_contrato(request, contrato_id):
    contrato = ContratoAnual.objects.get(pk=contrato_id)
    context = {
        'contrato': contrato
    }
    return render(request, 'contratos/pages/detalhes_contratos.html', context)


def atualizar_contrato(request, contrato_id):
    contrato = get_object_or_404(ContratoAnual, pk=contrato_id)
    form = ContratoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contratos/detalhes_contrato' + '/' +
                        str(contrato_id) + '/')
    context = {
        'contrato': contrato,
        'form': form
    }
    return render(request, 'contratos/pages/atualizar_contrato.html', context)


def apagar_contrato(request, contrato_id):
    contrato = get_object_or_404(ContratoAnual, pk=contrato_id)
    if request.method == 'POST':
        contrato.delete()
        return redirect('/contratos')
    context = {
        'contrato': contrato
    }
    return render(request, 'contratos/pages/apagar_contrato.html', context)
