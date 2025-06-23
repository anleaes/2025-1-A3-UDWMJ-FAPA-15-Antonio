from django.urls import path
from django.contrib import admin
from . import views

# Define o namespace da aplicação
app_name = 'core'

# Lista de caminhos da aplicação
urlpatterns = [
    path('', views.home, name='home'),  # Página inicial

    path('admin/', admin.site.urls),  # Acesso ao painel administrativo do Django

    # caminhos para Tipo de Vacina
    path('type/', views.list_type, name='list_type'),               
    path('type/add/', views.add_type, name='add_type'),             
    path('type/edit/<int:pk>/', views.edit_type, name='edit_type'), 
    path('type/delete/<int:pk>/', views.delete_type, name='delete_type'),  

    # caminhos para Fornecedores
    path('supplier/', views.list_supplier, name='list_supplier'),
    path('supplier/add/', views.add_supplier, name='add_supplier'),
    path('supplier/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('supplier/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),

    # caminhos para Vacinas
    path('vaccine/', views.list_vaccine, name='list_vaccine'),
    path('vaccine/add/', views.add_vaccine, name='add_vaccine'),
    path('vaccine/edit/<int:pk>/', views.edit_vaccine, name='edit_vaccine'),
    path('vaccine/delete/<int:pk>/', views.delete_vaccine, name='delete_vaccine'),

    # caminhos para Pessoas (pacientes)
    path('person/', views.list_person, name='list_person'),
    path('person/add/', views.add_person, name='add_person'),
    path('person/edit/<int:pk>/', views.edit_person, name='edit_person'),
    path('person/delete/<int:pk>/', views.delete_person, name='delete_person'),

    # caminhos para Clínicas
    path('clinic/', views.list_clinic, name='list_clinic'),
    path('clinic/add/', views.add_clinic, name='add_clinic'),
    path('clinic/edit/<int:pk>/', views.edit_clinic, name='edit_clinic'),
    path('clinic/delete/<int:pk>/', views.delete_clinic, name='delete_clinic'),

    # caminhos para Atendimentos (sessões de vacinação)
    path('session/', views.list_session, name='list_session'),
    path('session/add/', views.add_session, name='add_session'),
    path('session/edit/<int:pk>/', views.edit_session, name='edit_session'),
    path('session/delete/<int:pk>/', views.delete_session, name='delete_session'),
]
