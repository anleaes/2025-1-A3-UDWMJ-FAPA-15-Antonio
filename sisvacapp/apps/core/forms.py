from django import forms
from .models import Type, Supplier, Vaccine, Person, Clinic, Session

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            # Aplica 'form-select' em campos com seleção múltipla
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                # Aplica 'form-control' nos demais campos
                field.widget.attrs['class'] = 'form-control'


# Formulário para o modelo Type (Tipo de Vacina)
class TypeForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulário para o modelo Supplier (Fornecedor)
class SupplierForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})  # Campo de endereço com 1 linha
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulário para o modelo Vaccine (Vacina)
class VaccineForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})  # Descrição em textarea
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena os dados nos campos tipo e fornecedor
        self.fields['type'].queryset = Type.objects.order_by('description')
        self.fields['supplier'].queryset = Supplier.objects.order_by('name')


# Formulário para o modelo Person (Pessoa)
class PersonForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})  # Endereço em textarea
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulário para o modelo Clinic (Clínica)
class ClinicForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})  # Endereço em textarea
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulário para o modelo Session (Atendimento)
class SessionForm(BootstrapFormMixin, forms.ModelForm):
    # Campo de paciente com ordenação por nome
    patient = forms.ModelChoiceField(
        queryset=Person.objects.order_by('name'),
        label='Paciente'
    )

    # Campo para selecionar várias vacinas, ordenado por nome
    vaccines = forms.ModelMultipleChoiceField(
        queryset=Vaccine.objects.order_by('name'),
        widget=forms.SelectMultiple(),
        required=False,
        label='Vacinas aplicadas no atendimento'
    )

    class Meta:
        model = Session
        fields = ['session_date', 'clinic', 'patient', 'vaccines']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena a lista de clínicas
        self.fields['clinic'].queryset = Clinic.objects.order_by('name')

        # Se estiver editando um atendimento existente, mostra só as vacinas já associadas
        if self.instance and self.instance.pk:
            self.fields['vaccines'].queryset = self.instance.vaccines.all().order_by('name')
        else:
            self.fields['vaccines'].queryset = Vaccine.objects.order_by('name')

        # Remover a classe padrão do widget checkbox para manter checkbox bonitinho
        #(eu ia adicionar o campo checkbox (um widget) na edição do atendimento
        #  para permitir a remoção de uma vacina específica
        # mas tive problemas para fazer isso funcionar, então ficou uma versão provisória que para modificar
        # as vacinas é necessário excluir o atendimento e criar um novo)
