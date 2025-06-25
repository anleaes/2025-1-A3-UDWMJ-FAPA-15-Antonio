from django.urls import path
from . import views

app_name = 'administrationroute'

urlpatterns = [
    path('', views.list_administrationroute, name='list_administrationroute'),
    path('add/', views.add_administrationroute, name='add_administrationroute'),
    path('edit/<int:pk>/', views.edit_administrationroute, name='edit_administrationroute'),
    path('delete/<int:pk>/', views.delete_administrationroute, name='delete_administrationroute'),
]
