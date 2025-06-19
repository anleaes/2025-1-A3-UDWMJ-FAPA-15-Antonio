from django import forms
from .models import Type, Supplier, Vaccine, Person, Clinic, Vaccination, VaccineItem, Session

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = '__all__'

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'

class VaccineItemForm(forms.ModelForm):
    class Meta:
        model = VaccineItem
        fields = '__all__'

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'