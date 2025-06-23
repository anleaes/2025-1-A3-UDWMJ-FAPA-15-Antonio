from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import ProtectedError
from django.contrib import messages
from .models import Type, Supplier, Vaccine, Person, Clinic, Session
from .forms import TypeForm, SupplierForm, VaccineForm, PersonForm, ClinicForm, SessionForm


# -------- home -------- #
def home(request):
    return render(request, 'core/home.html')

# Função para listar registros de qualquer modelo
def list_entities(request, model, template_name, context_name):
    objetos = model.objects.all()
    context = {context_name: objetos}
    return render(request, template_name, context)

# Função para adicionar registros de qualquer modelo
def add_entity(request, form_class, template_name, redirect_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()  # SALVA RELACIONAMENTOS MANY TO MANY (vacinas por excemplo)
            return redirect(redirect_name)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

# Função para editar registros de qualquer modelo
def edit_entity(request, pk, model, form_class, template_name, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()  # SALVA RELACIONAMENTOS MANY TO MANY (mesmos exemplos do de cima)
            return redirect(redirect_name)
    else:
        form = form_class(instance=obj)
    return render(request, template_name, {'form': form})

# Função auxiliar para deletar registros de qualquer modelo
def delete_entity(request, pk, model, template_name, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_name)
    return render(request, template_name, {'object': obj})

# Função para listar registros de qualquer modelo com ordenação (ordem alfabética, para facilitar pra encontrar os dados)
def list_entities(request, model, template_name, context_name, ordering=None):
    objetos = model.objects.all()
    if ordering:
        objetos = objetos.order_by(ordering)
    context = {context_name: objetos}
    return render(request, template_name, context)

# -------- TYPE -------- #
def list_type(request):
    return list_entities(request, Type, 'type/list_type.html', 'types')

def add_type(request):
    return add_entity(request, TypeForm, 'type/add_type.html', 'core:list_type')

def edit_type(request, pk):
    return edit_entity(request, pk, Type, TypeForm, 'type/edit_type.html', 'core:list_type')

# Deleta um registro, pedindo confirmação antes
def delete_type(request, pk):
    type_obj = get_object_or_404(Type, pk=pk)
    has_protected_error = False
    if request.method == 'POST':
        try:
            type_obj.delete()
            messages.success(request, 'Tipo excluído com sucesso.')
            return redirect('core:list_type')
        except ProtectedError:
            messages.error(request, 'Não é possível excluir este tipo porque existem vacinas cadastradas que são deste tipo.')
            has_protected_error = True
    return render(request, 'type/delete_type.html', {'type': type_obj, 'has_protected_error': has_protected_error})

# -------- SUPPLIER -------- #
def list_supplier(request):
    return list_entities(request, Supplier, 'supplier/list_supplier.html', 'suppliers')

def add_supplier(request):
    return add_entity(request, SupplierForm, 'supplier/add_supplier.html', 'core:list_supplier')

def edit_supplier(request, pk):
    return edit_entity(request, pk, Supplier, SupplierForm, 'supplier/edit_supplier.html', 'core:list_supplier')

def delete_supplier(request, pk):
    return delete_entity(request, pk, Supplier, 'supplier/delete_supplier.html', 'core:list_supplier')

# -------- VACCINE -------- #
def list_vaccine(request):
    return list_entities(request, Vaccine, 'vaccine/list_vaccine.html', 'vaccines')

def add_vaccine(request):
    return add_entity(request, VaccineForm, 'vaccine/add_vaccine.html', 'core:list_vaccine')

def edit_vaccine(request, pk):
    return edit_entity(request, pk, Vaccine, VaccineForm, 'vaccine/edit_vaccine.html', 'core:list_vaccine')

def delete_vaccine(request, pk):
    return delete_entity(request, pk, Vaccine, 'vaccine/delete_vaccine.html', 'core:list_vaccine')

# -------- PERSON -------- #
def list_person(request):
    return list_entities(request, Person, 'person/list_person.html', 'persons')

def add_person(request):
    return add_entity(request, PersonForm, 'person/add_person.html', 'core:list_person')

def edit_person(request, pk):
    return edit_entity(request, pk, Person, PersonForm, 'person/edit_person.html', 'core:list_person')

def delete_person(request, pk):
    return delete_entity(request, pk, Person, 'person/delete_person.html', 'core:list_person')

# -------- CLINIC -------- #
def list_clinic(request):
    return list_entities(request, Clinic, 'clinic/list_clinic.html', 'clinics')

def add_clinic(request):
    return add_entity(request, ClinicForm, 'clinic/add_clinic.html', 'core:list_clinic')

def edit_clinic(request, pk):
    return edit_entity(request, pk, Clinic, ClinicForm, 'clinic/edit_clinic.html', 'core:list_clinic')

def delete_clinic(request, pk):
    return delete_entity(request, pk, Clinic, 'clinic/delete_clinic.html', 'core:list_clinic')

# -------- SESSION -------- #
def list_session(request):
    return list_entities(request, Session, 'session/list_session.html', 'sessions', ordering='-session_date')

def add_session(request):
    return add_entity(request, SessionForm, 'session/add_session.html', 'core:list_session')

def edit_session(request, pk):
    return edit_entity(request, pk, Session, SessionForm, 'session/edit_session.html', 'core:list_session')

def delete_session(request, pk):
    return delete_entity(request, pk, Session, 'session/delete_session.html', 'core:list_session')
