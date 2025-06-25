from apps.person.models import Person
from apps.person.forms import PersonForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection

def list_person(request):
    return list_entities(request, Person, 'person/list_person.html', 'persons')

def add_person(request):
    return add_entity(request, PersonForm, 'person/add_person.html', 'person:list_person')

def edit_person(request, pk):
    return edit_entity(request, pk, Person, PersonForm, 'person/edit_person.html', 'person:list_person')

def delete_person(request, pk):
    return delete_entity_with_protection(
        request, pk, Person, 'person/delete_person.html', 'person:list_person', 'Pessoa', 'person'
    )
