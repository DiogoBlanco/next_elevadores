from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'dashboard/pages/dashboard.html')
