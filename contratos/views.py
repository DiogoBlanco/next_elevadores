from django.shortcuts import render, redirect
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
