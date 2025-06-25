from django import forms

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
