from django import forms
from .models import Professional

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

# Formulário para o modelo Professional
class ProfessionalForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Professional  # Usa o modelo Professional
        fields = '__all__'   # Todos os campos do modelo
