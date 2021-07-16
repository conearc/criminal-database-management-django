from django.contrib import admin
from crime.models import Crime
from criminal.models import Criminal
from policestation.models import PoliceStation
from policeofficer.models import PoliceOfficer

# Register your models here.
admin.site.register(Crime)
admin.site.register(Criminal)
admin.site.register(PoliceStation)
admin.site.register(PoliceOfficer)
