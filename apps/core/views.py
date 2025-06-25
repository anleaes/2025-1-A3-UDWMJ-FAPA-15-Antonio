from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import ProtectedError
from django.contrib import messages
from django.db import connection

def disable_parallel_dml():
    with connection.cursor() as cursor:
        cursor.execute("ALTER SESSION DISABLE PARALLEL DML")

# Página inicial
def home(request):
    return render(request, 'core/home.html')

# Utilitários globais para uso dos apps:
def list_entities(request, model, template_name, context_name, ordering=None):
    objetos = model.objects.all()
    if ordering:
        objetos = objetos.order_by(ordering)
    context = {context_name: objetos}
    return render(request, template_name, context)

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

def delete_entity(request, pk, model, template_name, redirect_name):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(redirect_name)
    return render(request, template_name, {'object': obj})

def delete_entity_with_protection(request, pk, model, template_name, redirect_name, object_name, context_key):
    obj = get_object_or_404(model, pk=pk)
    has_protected_error = False
    is_deleted = False
    if request.method == 'POST':
        try:
            obj.delete()
            messages.success(request, f'{object_name} excluído(a) com sucesso.')
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

