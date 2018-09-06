from django.db import models

# Create your models here.

class PinCode(models.Model):
    place = models.CharField(max_length=120, blank=True)
    pincode = models.CharField(max_length=120, blank=True)
    office_Type = models.CharField(max_length=120, blank=True)
    Delivery_status = models.CharField(max_length=120, blank=True)
    division_name = models.CharField(max_length=120, blank=True)
    region_name = models.CharField(max_length=120, blank=True)
    circle_name =  models.CharField(max_length=120, blank=True)
    Taluk = models.CharField(max_length=120, blank=True)
    district = models.CharField(max_length=120, blank=True)
    state_name =  models.CharField(max_length=120, blank=True)
