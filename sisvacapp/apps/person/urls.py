from django.urls import path
from .views import list_person, add_person, edit_person, delete_person

app_name = 'person'

urlpatterns = [
    path('', list_person, name='list_person'),
    path('add/', add_person, name='add_person'),
    path('edit/<int:pk>/', edit_person, name='edit_person'),
    path('delete/<int:pk>/', delete_person, name='delete_person'),
]
