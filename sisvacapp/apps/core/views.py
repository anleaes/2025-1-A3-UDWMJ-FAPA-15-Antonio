from django.shortcuts import render, redirect, get_object_or_404
from .models import Type, Supplier, Vaccine, Person, Clinic, Vaccination, VaccineItem, Session
from .forms import TypeForm, SupplierForm, VaccineForm, PersonForm, ClinicForm, VaccinationForm, VaccineItemForm, SessionForm

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
            form.save()
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
            form.save()
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


# -------- TYPE -------- #
def list_type(request):
    return list_entities(request, Type, 'type/list_type.html', 'types')

def add_type(request):
    return add_entity(request, TypeForm, 'type/add_type.html', 'core:list_type')

def edit_type(request, pk):
    return edit_entity(request, pk, Type, TypeForm, 'type/edit_type.html', 'core:list_type')

def delete_type(request, pk):
    return delete_entity(request, pk, Type, 'type/delete_type.html', 'core:list_type')


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


# -------- VACCINATION -------- #
def list_vaccination(request):
    return list_entities(request, Vaccination, 'vaccination/list_vaccination.html', 'vaccinations')

def add_vaccination(request):
    return add_entity(request, VaccinationForm, 'vaccination/add_vaccination.html', 'core:list_vaccination')

def edit_vaccination(request, pk):
    return edit_entity(request, pk, Vaccination, VaccinationForm, 'vaccination/edit_vaccination.html', 'core:list_vaccination')

def delete_vaccination(request, pk):
    return delete_entity(request, pk, Vaccination, 'vaccination/delete_vaccination.html', 'core:list_vaccination')


# -------- VACCINE ITEM -------- #
def list_vaccineitem(request):
    return list_entities(request, VaccineItem, 'vaccineitem/list_vaccineitem.html', 'vaccineitems')

def add_vaccineitem(request):
    return add_entity(request, VaccineItemForm, 'vaccineitem/add_vaccineitem.html', 'core:list_vaccineitem')

def edit_vaccineitem(request, pk):
    return edit_entity(request, pk, VaccineItem, VaccineItemForm, 'vaccineitem/edit_vaccineitem.html', 'core:list_vaccineitem')

def delete_vaccineitem(request, pk):
    return delete_entity(request, pk, VaccineItem, 'vaccineitem/delete_vaccineitem.html', 'core:list_vaccineitem')


# -------- SESSION -------- #
def list_session(request):
    return list_entities(request, Session, 'session/list_session.html', 'sessions')

def add_session(request):
    return add_entity(request, SessionForm, 'session/add_session.html', 'core:list_session')

def edit_session(request, pk):
    return edit_entity(request, pk, Session, SessionForm, 'session/edit_session.html', 'core:list_session')

def delete_session(request, pk):
    return delete_entity(request, pk, Session, 'session/delete_session.html', 'core:list_session')
