from django import forms
from .models import AdministrationRoute

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

# Formulário para via de administração
class AdministrationRouteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = AdministrationRoute
        fields = ['name']
