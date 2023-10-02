from django.urls import path
from . import views

app_name = 'contratos'

urlpatterns = [
    path('', views.contratos_home, name='contratos'),
    path('criar_contrato/', views.criar_contrato, name='criar_contrato'),
    path('detalhes_contrato/<int:contrato_id>/', views.detalhes_contrato,
         name='detalhes_contrato'),
    path('atualizar/<int:contrato_id>/',
         views.atualizar_contrato,
         name='atualizar_contrato'),
    path('apagar/<int:contrato_id>/',
         views.apagar_contrato,
         name='apagar_contrato'),
]
