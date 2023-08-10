from django.shortcuts import render, redirect
from .models import Customer, ModernizationContract, Contract
from .forms import CustomerForm


def home(request):
    return render(request, 'home/home.html')


def customers(request):
    clients = Customer.objects.all()
    return render(request, 'home/customers.html', context={'clients': clients})


def save_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            return redirect('clientes')
    else:
        form = CustomerForm()
    return render(request, 'home/save_customer.html', context={'form': form})
