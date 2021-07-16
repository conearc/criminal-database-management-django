from django.db import models

# Create your models here.


# Model having all criminal Details

class Criminal(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    contactno = models.CharField(max_length=10, blank=True, null=True)
    special_feature = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='criminal/images', blank=True)

    def __str__(self):
        return self.name
