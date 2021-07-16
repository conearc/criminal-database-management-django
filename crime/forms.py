from django.forms import ModelForm
from .models import *

# Form for Crime Detail Entry


class CrimeForm(ModelForm):
    class Meta:
        model = Crime
        fields = '__all__'
