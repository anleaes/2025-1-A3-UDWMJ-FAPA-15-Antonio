from apps.professional.models import Professional
from apps.professional.forms import ProfessionalForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection

def list_professional(request):
    return list_entities(request, Professional, 'professional/list_professional.html', 'professionals')

def add_professional(request):
    return add_entity(request, ProfessionalForm, 'professional/add_professional.html', 'professional:list_professional')

def edit_professional(request, pk):
    return edit_entity(request, pk, Professional, ProfessionalForm, 'professional/edit_professional.html', 'professional:list_professional')

def delete_professional(request, pk):
    return delete_entity_with_protection(
        request, pk, Professional, 'professional/delete_professional.html', 'professional:list_professional', 'Profissional', 'object'
    )
