from django import forms
from .models import Session
from apps.person.models import Person
from apps.vaccine.models import Vaccine
from apps.clinic.models import Clinic
from apps.professional.models import Professional
from apps.administrationroute.models import AdministrationRoute

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

# Formulário para o modelo Session (Atendimento)
class SessionForm(BootstrapFormMixin, forms.ModelForm):
    patient = forms.ModelChoiceField(
        queryset=Person.objects.order_by('name'),
        label='Paciente'
    )
    vaccines = forms.ModelMultipleChoiceField(
        queryset=Vaccine.objects.order_by('name'),
        widget=forms.SelectMultiple(),
        required=False,
        label='Vacinas aplicadas no atendimento'
    )
    professional = forms.ModelChoiceField(
        queryset=Professional.objects.order_by('name'),
        required=False,
        label='Profissional responsável'
    )
    administration_route = forms.ModelChoiceField(
        queryset=AdministrationRoute.objects.order_by('name'),
        required=False,
        label='Via de administração'
    )
    class Meta:
        model = Session
        fields = ['session_date', 'clinic', 'patient', 'vaccines', 'professional', 'administration_route']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clinic'].queryset = Clinic.objects.order_by('name')
        self.fields['professional'].queryset = Professional.objects.order_by('name')
        self.fields['administration_route'].queryset = AdministrationRoute.objects.order_by('name')
        if self.instance and self.instance.pk:
            self.fields['vaccines'].queryset = self.instance.vaccines.all().order_by('name')
        else:
            self.fields['vaccines'].queryset = Vaccine.objects.order_by('name')
