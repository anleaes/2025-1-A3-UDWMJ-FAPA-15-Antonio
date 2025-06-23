from django import forms
from .models import Type, Supplier, Vaccine, Person, Clinic, Vaccination, Session

# Mixin para adicionar classes Bootstrap aos campos automaticamente
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class TypeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

class SupplierForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class VaccineForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = '__all__'

class PersonForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }

class ClinicForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'

class VaccinationForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'

class SessionForm(BootstrapFormMixin, forms.ModelForm):
    # Campo para selecionar o paciente (pessoa)
    patient = forms.ModelChoiceField(
        queryset=Person.objects.all(),
        label='Paciente',
        empty_label='Selecione o paciente'
    )

    # Campo pra selecionar uma ou mais vacinas aplicadas no atendimento
    vaccines = forms.ModelMultipleChoiceField(
    queryset=Vaccine.objects.all(),
    widget=forms.CheckboxSelectMultiple,
    label='Vacinas aplicadas'
)

    class Meta:
        model = Session
        # Os campos do modelo (sem vaccines e patient que são extras)
        fields = ['session_date', 'clinic']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


        self.fields['vaccines'].widget.attrs.pop('class', None)
