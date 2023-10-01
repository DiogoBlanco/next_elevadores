from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.clientes_home, name='clientes'),
    path('criar_cliente_cpf/', views.criar_cliente_cpf,
         name='criar_cliente_cpf'),
    path('criar_cliente_cnpj/', views.criar_cliente_cnpj,
         name='criar_cliente_cnpj'),
    path('detalhes_cliente/<int:cliente_id>/', views.detalhes_cliente,
         name='detalhes_cliente'),
    path('atualizar/<int:cliente_id>/',
         views.atualizar_cliente,
         name='atualizar_cliente'),
    path('apagar/<int:cliente_id>/',
         views.apagar_cliente,
         name='apagar_cliente'),
]
