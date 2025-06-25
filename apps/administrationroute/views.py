from apps.administrationroute.models import AdministrationRoute
from apps.administrationroute.forms import AdministrationRouteForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection

def list_administrationroute(request):
    return list_entities(request, AdministrationRoute, 'administrationroute/list_administrationroute.html', 'routes')

def add_administrationroute(request):
    return add_entity(request, AdministrationRouteForm, 'administrationroute/add_administrationroute.html', 'administrationroute:list_administrationroute')

def edit_administrationroute(request, pk):
    return edit_entity(request, pk, AdministrationRoute, AdministrationRouteForm, 'administrationroute/edit_administrationroute.html', 'administrationroute:list_administrationroute')

def delete_administrationroute(request, pk):
    return delete_entity_with_protection(
        request, pk, AdministrationRoute, 'administrationroute/delete_administrationroute.html', 'administrationroute:list_administrationroute', 'Via de administração', 'object'
    )
