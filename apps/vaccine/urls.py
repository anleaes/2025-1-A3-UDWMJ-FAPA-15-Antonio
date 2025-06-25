from django.urls import path
from .views import list_vaccine, add_vaccine, edit_vaccine, delete_vaccine

app_name = 'vaccine'

urlpatterns = [
    path('', list_vaccine, name='list_vaccine'),
    path('add/', add_vaccine, name='add_vaccine'),
    path('edit/<int:pk>/', edit_vaccine, name='edit_vaccine'),
    path('delete/<int:pk>/', delete_vaccine, name='delete_vaccine'),
]
