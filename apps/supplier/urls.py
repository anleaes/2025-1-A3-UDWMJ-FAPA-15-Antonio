from django.urls import path
from .views import list_supplier, add_supplier, edit_supplier, delete_supplier

app_name = 'supplier'

urlpatterns = [
    path('', list_supplier, name='list_supplier'),
    path('add/', add_supplier, name='add_supplier'),
    path('edit/<int:pk>/', edit_supplier, name='edit_supplier'),
    path('delete/<int:pk>/', delete_supplier, name='delete_supplier'),
]
