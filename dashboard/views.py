from django.shortcuts import render
from clientes.models import Cliente, ClientePF, ClientePJ
from contratos.models import ContratoAnual, TipoContrato
from django.db.models import Q
from .forms import BuscaForm


def home(request):
    qtd_clientes = Cliente.objects.count()
    qtd_contratos = ContratoAnual.objects.count()

    context = {
        'qtd_clientes': qtd_clientes,
        'qtd_contratos': qtd_contratos,
    }
    return render(request, 'dashboard/pages/dashboard.html', context)


def buscar(request):
    if request.method == 'GET':
        form = BuscaForm(request.GET)
        if form.is_valid():
            busca = form.cleaned_data['busca']
            resultados_cliente = Cliente.objects.filter(
                Q(nome__icontains=busca) |
                Q(id__icontains=busca) |
                Q(sobrenome__icontains=busca)
            )
            resultados_contrato = ContratoAnual.objects.filter(
                Q(data_de_renovacao__icontains=busca) |
                Q(id__icontains=busca) |
                Q(marca_dos_elevadores__icontains=busca)
            )
    else:
        form = BuscaForm()

    return render(request, 'dashboard/pages/busca.html',
                  {'form': form, 'resultados_cliente': resultados_cliente,
                   'resultados_contrato': resultados_contrato
                   })
