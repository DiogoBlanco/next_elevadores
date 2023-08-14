from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customer_list, name='customers'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer'),
    path('customers/create_customer',
         views.create_customer, name='create_customer'),
    path('customers/<int:customer_id>/update',
         views.update_customer, name='update_customer'),
]
