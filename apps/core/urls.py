from django.urls import path
from . import views

# Define o namespace da aplicação
app_name = 'core'

# Lista de caminhos da aplicação
urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
]
