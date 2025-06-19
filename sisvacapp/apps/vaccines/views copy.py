from django.shortcuts import render, redirect
from .models import Type, Supplier, Vaccine, Person, Clinic, Vaccination, VaccineItem, Session
from .forms import TypeForm, SupplierForm, VaccineForm, PersonForm, ClinicForm, VaccinationForm, VaccineItemForm, SessionForm


# -------- home -------- #
def home(request):
    return render(request, 'core/home.html')


# -------- TYPE -------- #
def add_type(request):
    template_name = 'type/add_type.html'
    context = {}
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = TypeForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- SUPPLIER -------- #
def add_supplier(request):
    template_name = 'supplier/add_supplier.html'
    context = {}
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = SupplierForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- VACCINE -------- #
def add_vaccine(request):
    template_name = 'vaccine/add_vaccine.html'
    context = {}
    if request.method == 'POST':
        form = VaccineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = VaccineForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- PERSON -------- #
def add_person(request):
    template_name = 'person/add_person.html'
    context = {}
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = PersonForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- CLINIC -------- #
def add_clinic(request):
    template_name = 'clinic/add_clinic.html'
    context = {}
    if request.method == 'POST':
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ClinicForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- VACCINATION -------- #
def add_vaccination(request):
    template_name = 'vaccination/add_vaccination.html'
    context = {}
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = VaccinationForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- VACCINE ITEM -------- #
def add_vaccine_item(request):
    template_name = 'vaccineitem/add_vaccine_item.html'
    context = {}
    if request.method == 'POST':
        form = VaccineItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = VaccineItemForm()
    context['form'] = form
    return render(request, template_name, context)


# -------- SESSION -------- #
def add_session(request):
    template_name = 'session/add_session.html'
    context = {}
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = SessionForm()
    context['form'] = form
    return render(request, template_name, context)