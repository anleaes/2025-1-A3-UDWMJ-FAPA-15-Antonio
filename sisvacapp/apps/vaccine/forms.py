from django import forms
from .models import Vaccine
from apps.type.models import Type
from apps.supplier.models import Supplier

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

# Formulário para o modelo Vaccine (Vacina)
class VaccineForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].queryset = Type.objects.order_by('description')
        self.fields['supplier'].queryset = Supplier.objects.order_by('name')
