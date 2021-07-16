from django.db import models


class PoliceOfficer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    height = models.IntegerField()
    home_address = models.CharField(max_length=250)
    contactno = models.CharField(max_length=10)

    def __str__(self):
        return self.name
