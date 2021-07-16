from django.forms import ModelForm
from .models import *

# Form for PoliceStation Detail Entry


class PoliceStationForm(ModelForm):
    class Meta:
        model = PoliceStation
        fields = '__all__'
