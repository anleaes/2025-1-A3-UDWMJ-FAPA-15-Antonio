from django.urls import path
from . import views

app_name = 'professional'

urlpatterns = [
    path('', views.list_professional, name='list_professional'),  # Lista profissionais
    path('add/', views.add_professional, name='add_professional'),  # Adiciona profissional
    path('edit/<int:pk>/', views.edit_professional, name='edit_professional'),  # Edita profissional
    path('delete/<int:pk>/', views.delete_professional, name='delete_professional'),  # Remove profissional
]
