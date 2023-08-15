from django.shortcuts import render, redirect, get_object_or_404
from .forms import BudgetForm
from .models import Budget
from home.models import Customer


def create_budget(request):
    form = BudgetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/budgets')
    context = {
        'form': form
    }
    return render(request, 'budgets/budget_form.html', context)


def budgets_list(request):
    budgets = Budget.objects.all()
    context = {
        'budgets': budgets
    }
    return render(request, 'budgets/budgets_list.html', context)


def budget_detail(request, budget_id):
    budget = get_object_or_404(
        Budget, pk=budget_id)
    customer = Customer.objects.all()
    context = {
        'budget': budget,
        'customer': customer,
    }
    return render(request, 'budgets/budget_detail.html', context)
