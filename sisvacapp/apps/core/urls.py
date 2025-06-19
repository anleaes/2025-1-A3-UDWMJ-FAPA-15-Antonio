from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    path('admin/', admin.site.urls),

    path('type/', views.list_type, name='list_type'),
    path('type/add/', views.add_type, name='add_type'),
    path('type/edit/<int:pk>/', views.edit_type, name='edit_type'),
    path('type/delete/<int:pk>/', views.delete_type, name='delete_type'),

    path('supplier/', views.list_supplier, name='list_supplier'),
    path('supplier/add/', views.add_supplier, name='add_supplier'),
    path('supplier/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('supplier/delete/<int:pk>/', views.delete_supplier, name='delete_supplier'),

    path('vaccine/', views.list_vaccine, name='list_vaccine'),
    path('vaccine/add/', views.add_vaccine, name='add_vaccine'),
    path('vaccine/edit/<int:pk>/', views.edit_vaccine, name='edit_vaccine'),
    path('vaccine/delete/<int:pk>/', views.delete_vaccine, name='delete_vaccine'),

    path('person/', views.list_person, name='list_person'),
    path('person/add/', views.add_person, name='add_person'),
    path('person/edit/<int:pk>/', views.edit_person, name='edit_person'),
    path('person/delete/<int:pk>/', views.delete_person, name='delete_person'),

    path('clinic/', views.list_clinic, name='list_clinic'),
    path('clinic/add/', views.add_clinic, name='add_clinic'),
    path('clinic/edit/<int:pk>/', views.edit_clinic, name='edit_clinic'),
    path('clinic/delete/<int:pk>/', views.delete_clinic, name='delete_clinic'),

    path('vaccination/', views.list_vaccination, name='list_vaccination'),
    path('vaccination/add/', views.add_vaccination, name='add_vaccination'),
    path('vaccination/edit/<int:pk>/', views.edit_vaccination, name='edit_vaccination'),
    path('vaccination/delete/<int:pk>/', views.delete_vaccination, name='delete_vaccination'),

    path('vaccineitem/', views.list_vaccineitem, name='list_vaccineitem'),
    path('vaccineitem/add/', views.add_vaccineitem, name='add_vaccineitem'),
    path('vaccineitem/edit/<int:pk>/', views.edit_vaccineitem, name='edit_vaccineitem'),
    path('vaccineitem/delete/<int:pk>/', views.delete_vaccineitem, name='delete_vaccineitem'),

    path('session/', views.list_session, name='list_session'),
    path('session/add/', views.add_session, name='add_session'),
    path('session/edit/<int:pk>/', views.edit_session, name='edit_session'),
    path('session/delete/<int:pk>/', views.delete_session, name='delete_session'),
]
