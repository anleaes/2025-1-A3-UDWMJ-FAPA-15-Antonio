from django.urls import path
from .views import list_session, add_session, edit_session, delete_session

app_name = 'session'

urlpatterns = [
    path('', list_session, name='list_session'),
    path('add/', add_session, name='add_session'),
    path('edit/<int:pk>/', edit_session, name='edit_session'),
    path('delete/<int:pk>/', delete_session, name='delete_session'),
]
