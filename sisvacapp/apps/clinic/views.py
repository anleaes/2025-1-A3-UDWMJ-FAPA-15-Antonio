from apps.clinic.models import Clinic
from apps.clinic.forms import ClinicForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection

def list_clinic(request):
    return list_entities(request, Clinic, 'clinic/list_clinic.html', 'clinics')

def add_clinic(request):
    return add_entity(request, ClinicForm, 'clinic/add_clinic.html', 'clinic:list_clinic')

def edit_clinic(request, pk):
    return edit_entity(request, pk, Clinic, ClinicForm, 'clinic/edit_clinic.html', 'clinic:list_clinic')

def delete_clinic(request, pk):
    return delete_entity_with_protection(
        request, pk, Clinic, 'clinic/delete_clinic.html', 'clinic:list_clinic', 'Clínica', 'clinic'
    )
