from apps.vaccine.models import Vaccine
from apps.vaccine.forms import VaccineForm
from apps.session.models import Session
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection
from django.db import connection

def list_vaccine(request):
    return list_entities(request, Vaccine, 'vaccine/list_vaccine.html', 'vaccines')

def add_vaccine(request):
    return add_entity(request, VaccineForm, 'vaccine/add_vaccine.html', 'vaccine:list_vaccine')

def edit_vaccine(request, pk):
    return edit_entity(request, pk, Vaccine, VaccineForm, 'vaccine/edit_vaccine.html', 'vaccine:list_vaccine')

def delete_vaccine(request, pk):
    if connection.vendor == 'oracle':
        with connection.cursor() as cursor:
            cursor.execute("ALTER SESSION DISABLE PARALLEL DML")
    vaccine = get_object_or_404(Vaccine, pk=pk)
    if request.method == 'POST' and Session.objects.filter(vaccines=vaccine).exists():
        messages.error(request, "Não é possível excluir esta vacina porque ela está associada a atendimentos.")
        return render(request, 'vaccine/delete_vaccine.html', {
            'vaccine': vaccine,
            'has_protected_error': True,
            'is_deleted': False,
        })
    return delete_entity_with_protection(
        request, pk, Vaccine, 'vaccine/delete_vaccine.html', 'vaccine:list_vaccine', 'Vacina', 'vaccine'
    )
