from django.urls import path
from . import views

app_name = 'budgets'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.create_budget, name='budgets')
]
