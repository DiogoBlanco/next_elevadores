import io
from django.shortcuts import render, redirect
from .forms import BudgetForm
from django.http import FileResponse
from reportlab.pdfgen import canvas


def index(request):
    return render(request, 'budgets/index.html')


def create_budget(request):
    form = BudgetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/budgets')
    context = {
        'form': form
    }
    return render(request, 'budgets/budget_form.html', context)
