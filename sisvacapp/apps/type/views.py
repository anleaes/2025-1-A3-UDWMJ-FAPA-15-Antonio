from apps.type.models import Type
from apps.type.forms import TypeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection

def list_type(request):
    return list_entities(request, Type, 'type/list_type.html', 'types')

def add_type(request):
    return add_entity(request, TypeForm, 'type/add_type.html', 'type:list_type')

def edit_type(request, pk):
    return edit_entity(request, pk, Type, TypeForm, 'type/edit_type.html', 'type:list_type')

def delete_type(request, pk):
    return delete_entity_with_protection(
        request, pk, Type, 'type/delete_type.html', 'type:list_type', 'Tipo', 'type'
    )
