from django import forms
from .models import Supplier

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

# Formulário para o modelo Supplier (Fornecedor)
class SupplierForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
