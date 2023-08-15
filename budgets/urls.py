from django.urls import path
from . import views

app_name = 'budgets'

urlpatterns = [
    path('create_budget/', views.create_budget, name='create_budgets'),
    path('', views.budgets_list, name='budgets'),
    path('<int:budget_id>/', views.budget_detail, name='budget'),
]
