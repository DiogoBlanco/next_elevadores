from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.customers, name='clientes'),
    path('clientes/novo_cliente', views.save_customer, name='novo_cliente'),
]
