from django import forms
from .models import Person

# Mixin para aplicar classes do Bootstrap nos campos dos formulários
class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field.widget, forms.SelectMultiple):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

# Formulário para o modelo Person (Pessoa)
class PersonForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1})
        } # limitando o campo de endereço a 1 linha

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
