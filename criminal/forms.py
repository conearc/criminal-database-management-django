from django.forms import ModelForm
from django import forms
from .models import *

# Form for Criminal Detail Entry


class CriminalForm(ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'


class SearchCriminalForm(forms.Form):
    image = forms.FileField()
