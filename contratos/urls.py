from django.urls import path
from . import views

app_name = 'contratos'

urlpatterns = [
    path('', views.contratos_home, name='contratos'),
    path('criar_contrato/', views.criar_contrato, name='criar_contrato'),
]
