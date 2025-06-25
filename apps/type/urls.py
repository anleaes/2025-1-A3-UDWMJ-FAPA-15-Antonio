from django.urls import path
from .views import list_type, add_type, edit_type, delete_type

app_name = 'type'

urlpatterns = [
    path('', list_type, name='list_type'),
    path('add/', add_type, name='add_type'),
    path('edit/<int:pk>/', edit_type, name='edit_type'),
    path('delete/<int:pk>/', delete_type, name='delete_type'),
]
