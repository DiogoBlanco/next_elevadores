from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.clientes_home, name='clientes'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente'),
]
