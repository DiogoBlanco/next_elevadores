from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, ModernizationContract, Contract
from .forms import CustomerForm


def home(request):
    return render(request, 'home/home.html')


def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers,
    }
    return render(request, 'home/customer_list.html', context)


def customer_detail(request, customer_id):
    customer = get_object_or_404(
        Customer, pk=customer_id
    )
    context = {
        'customer': customer,
    }
    return render(request, 'home/customer_detail.html', context)


def create_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/customers')
    context = {
        'form': form
    }
    return render(request, 'home/customer_form.html', context)
