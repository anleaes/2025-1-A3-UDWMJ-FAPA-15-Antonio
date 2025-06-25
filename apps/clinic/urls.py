from django.urls import path
from .views import list_clinic, add_clinic, edit_clinic, delete_clinic

app_name = 'clinic'

urlpatterns = [
    path('', list_clinic, name='list_clinic'),
    path('add/', add_clinic, name='add_clinic'),
    path('edit/<int:pk>/', edit_clinic, name='edit_clinic'),
    path('delete/<int:pk>/', delete_clinic, name='delete_clinic'),
]
