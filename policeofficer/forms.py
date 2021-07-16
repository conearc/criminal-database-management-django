from django.forms import ModelForm
from .models import *

# Form for PoliceOfficer Detail Entry


class PoliceOfficerForm(ModelForm):
    class Meta:
        model = PoliceOfficer
        fields = '__all__'
