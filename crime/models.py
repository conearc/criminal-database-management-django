from django.db import models
from criminal.models import Criminal
from policeofficer.models import PoliceOfficer
from policestation.models import PoliceStation
# Create your models here.
# Model having Crime Details


class Crime(models.Model):
    firno = models.IntegerField()
    detail = models.CharField(max_length=4000)
    firno = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    complainent_name = models.CharField(max_length=100)
    complainent_address = models.CharField(max_length=500)
    policestation = models.ForeignKey(
        to=PoliceStation, on_delete=models.CASCADE)
    investigation_detail = models.CharField(max_length=4000)
    investigating_officer = models.ForeignKey(
        to=PoliceOfficer, on_delete=models.CASCADE)
    criminals = models.ManyToManyField(
        to=Criminal, related_query_name="crime", related_name="criminal")
