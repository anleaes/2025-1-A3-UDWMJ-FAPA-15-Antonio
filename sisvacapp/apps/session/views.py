from apps.session.models import Session
from apps.session.forms import SessionForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.core.views import list_entities, add_entity, edit_entity

def list_session(request):
    return list_entities(request, Session, 'session/list_session.html', 'sessions', ordering='-session_date')

def add_session(request):
    return add_entity(request, SessionForm, 'session/add_session.html', 'session:list_session')

def edit_session(request, pk):
    return edit_entity(request, pk, Session, SessionForm, 'session/edit_session.html', 'session:list_session')

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
        'has_protected_error': False,  # não precisa de proteção aqui pq não tem dependências diretas, é a ponta da cadeia
    })
