from django import forms
from .models import registration, reference


class registerationForms(forms.ModelForm):
    class Meta:
        model = registration
        fields = ['name', 'email', 'message', 'image']


class refereceForms(forms.ModelForm):
    class Meta:
        model = reference
        fields = ['author', 'pub_date']
