from apps.supplier.models import Supplier
from apps.supplier.forms import SupplierForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity, delete_entity_with_protection

def list_supplier(request):
    return list_entities(request, Supplier, 'supplier/list_supplier.html', 'suppliers')

def add_supplier(request):
    return add_entity(request, SupplierForm, 'supplier/add_supplier.html', 'supplier:list_supplier')

def edit_supplier(request, pk):
    return edit_entity(request, pk, Supplier, SupplierForm, 'supplier/edit_supplier.html', 'supplier:list_supplier')

def delete_supplier(request, pk):
    return delete_entity_with_protection(
        request, pk, Supplier, 'supplier/delete_supplier.html', 'supplier:list_supplier', 'Fornecedor', 'supplier'
    )
