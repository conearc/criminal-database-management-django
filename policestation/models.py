from django.db import models

# Model having Police Station Details


class PoliceStation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    contactno = models.CharField(max_length=10, blank=True, null=True)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.name
