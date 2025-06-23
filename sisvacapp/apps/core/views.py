from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import ProtectedError
from django.contrib import messages
from .models import Type, Supplier, Vaccine, Person, Clinic, Session
from .forms import TypeForm, SupplierForm, VaccineForm, PersonForm, ClinicForm, SessionForm
from django.db import connection

def disable_parallel_dml():
    with connection.cursor() as cursor:
        cursor.execute("ALTER SESSION DISABLE PARALLEL DML")

# Página inicial
def home(request):
    return render(request, 'core/home.html')

# Lista objetos de um modelo e renderiza template
def list_entities(request, model, template_name, context_name, ordering=None):
    objetos = model.objects.all()
    if ordering:
        objetos = objetos.order_by(ordering)
    context = {context_name: objetos}
    return render(request, template_name, context)

# Adiciona um novo registro via formulário
def add_entity(request, form_class, template_name, redirect_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()  # Salva relacionamentos ManyToMany
            return redirect(redirect_name)
    else:
        form = form_class()
    return render(request, template_name, {'form': form})

# Edita um registro existente via formulário
def edit_entity(request, pk, model, form_class, template_name, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            return redirect(redirect_name)
    else:
        form = form_class(instance=obj)
    return render(request, template_name, {'form': form})

# Deleta um registro simples
def delete_entity(request, pk, model, template_name, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_name)
    return render(request, template_name, {'object': obj})

# Essa fgunção testa se o objeto está associado a outro registro antes de deletar, e caso esteja relacionado, 
# exibe uma mensagem de erro e redireciona para a lista

def delete_entity_with_protection(request, pk, model, template_name, redirect_name, object_name, context_key):
    obj = get_object_or_404(model, pk=pk)
    has_protected_error = False
    is_deleted = False

    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, f'{object_name} excluído com sucesso.')
            is_deleted = True
        except ProtectedError:
            messages.error(request, f'Não é possível excluir este(a) {object_name.lower()} porque está associado(a) a outro registro.')
            has_protected_error = True

    context = {
        context_key: obj,
        'has_protected_error': has_protected_error,
        'is_deleted': is_deleted,
    }
    return render(request, template_name, context)

# -------- TYPE -------- #
def list_type(request):
    return list_entities(request, Type, 'type/list_type.html', 'types')

def add_type(request):
    return add_entity(request, TypeForm, 'type/add_type.html', 'core:list_type')

def edit_type(request, pk):
    return edit_entity(request, pk, Type, TypeForm, 'type/edit_type.html', 'core:list_type')

def delete_type(request, pk):
    return delete_entity_with_protection(
        request, pk, Type, 'type/delete_type.html', 'core:list_type', 'Tipo', 'type'
    )

# -------- SUPPLIER -------- #
def list_supplier(request):
    return list_entities(request, Supplier, 'supplier/list_supplier.html', 'suppliers')

def add_supplier(request):
    return add_entity(request, SupplierForm, 'supplier/add_supplier.html', 'core:list_supplier')

def edit_supplier(request, pk):
    return edit_entity(request, pk, Supplier, SupplierForm, 'supplier/edit_supplier.html', 'core:list_supplier')

def delete_supplier(request, pk):
    return delete_entity_with_protection(
        request, pk, Supplier, 'supplier/delete_supplier.html', 'core:list_supplier', 'Fornecedor', 'supplier'
    )

# -------- VACCINE -------- #
def list_vaccine(request):
    return list_entities(request, Vaccine, 'vaccine/list_vaccine.html', 'vaccines')

def add_vaccine(request):
    return add_entity(request, VaccineForm, 'vaccine/add_vaccine.html', 'core:list_vaccine')

def edit_vaccine(request, pk):
    return edit_entity(request, pk, Vaccine, VaccineForm, 'vaccine/edit_vaccine.html', 'core:list_vaccine')

def delete_vaccine(request, pk):
    from django.db import connection
    # Desabilita o paralelo para não dar erro bno Oracle 
    if connection.vendor == 'oracle':
        with connection.cursor() as cursor:
            cursor.execute("ALTER SESSION DISABLE PARALLEL DML")

    vaccine = get_object_or_404(Vaccine, pk=pk)
    # Verifica se está associada a algum atendimento (ManyToMany)
    if request.method == 'POST' and Session.objects.filter(vaccines=vaccine).exists():
        messages.error(request, "Não é possível excluir esta vacina porque ela está associada a atendimentos.")
        return render(request, 'vaccine/delete_vaccine.html', {
            'vaccine': vaccine,
            'has_protected_error': True,
            'is_deleted': False,
        })
    return delete_entity_with_protection(
        request, pk, Vaccine, 'vaccine/delete_vaccine.html', 'core:list_vaccine', 'Vacina', 'vaccine'
    )

# -------- PERSON -------- #
def list_person(request):
    return list_entities(request, Person, 'person/list_person.html', 'persons')

def add_person(request):
    return add_entity(request, PersonForm, 'person/add_person.html', 'core:list_person')

def edit_person(request, pk):
    return edit_entity(request, pk, Person, PersonForm, 'person/edit_person.html', 'core:list_person')

def delete_person(request, pk):
    return delete_entity_with_protection(
        request, pk, Person, 'person/delete_person.html', 'core:list_person', 'Pessoa', 'person'
    )

# -------- CLINIC -------- #
def list_clinic(request):
    return list_entities(request, Clinic, 'clinic/list_clinic.html', 'clinics')

def add_clinic(request):
    return add_entity(request, ClinicForm, 'clinic/add_clinic.html', 'core:list_clinic')

def edit_clinic(request, pk):
    return edit_entity(request, pk, Clinic, ClinicForm, 'clinic/edit_clinic.html', 'core:list_clinic')

def delete_clinic(request, pk):
    return delete_entity_with_protection(
        request, pk, Clinic, 'clinic/delete_clinic.html', 'core:list_clinic', 'Clínica', 'clinic'
    )

# -------- SESSION -------- #
def list_session(request):
    return list_entities(request, Session, 'session/list_session.html', 'sessions', ordering='-session_date')

def add_session(request):
    return add_entity(request, SessionForm, 'session/add_session.html', 'core:list_session')

def edit_session(request, pk):
    return edit_entity(request, pk, Session, SessionForm, 'session/edit_session.html', 'core:list_session')

# Deleta uma sessão, não tem necessidadede verificar se tem alfguma dependência, pois é a "ponta"

def delete_session(request, pk):
    session = get_object_or_404(Session, pk=pk)
    is_deleted = False

    if request.method == 'POST':
        session.delete()
        messages.success(request, "Atendimento excluído com sucesso.")
        is_deleted = True

    return render(request, 'session/delete_session.html', {
        'session': session,
        'is_deleted': is_deleted,
        'has_protected_error': False,  # não tem proteção aqui
    })

