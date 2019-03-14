from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Turbine(models.Model):

    #def __str__(self):
    #    return str(self.id+self.name+self.owner_id+self.rental_price)#self.type+self.owner_id+self.date_made+self.rental_price)

    park_name = models.CharField(max_length=40)
    disp_name = models.CharField(max_length=40)
    firm_name = models.CharField(max_length=40)
    turbine_type = models.CharField(max_length=40)
    control_type = models.CharField(max_length=10)
    #supported_by = models.CharField(max_length=20)
    turbine_power = models.FloatField()
    turbine_id = models.CharField(max_length=20)
    output_name = models.CharField(max_length=30)
    station_name = models.CharField(max_length=20)
    gru_name = models.CharField(max_length=25)
    sot_firm = models.CharField(max_length=20)
    sot_name = models.CharField(max_length=10)
    forecaster = models.CharField(max_length=20)
    isp_name = models.CharField(max_length=20)

    def __str__(self):
        return self.turbine_id

    class Meta:
        verbose_name_plural = 'турбини'


class TechGroup(models.Model):
    techgroup_name = models.CharField(max_length=20)

    def __str__(self):
        return self.techgroup_name

    class Meta:
        verbose_name_plural = 'работни групи'

class Technician(models.Model):
    technician_name = models.CharField(max_length=20)
    technician_techgroup = models.ForeignKey(TechGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.technician_name

    class Meta:
        verbose_name_plural = 'техници'
        

class Repair(models.Model):
    turbine = models.ForeignKey(Turbine, on_delete=models.CASCADE)
    repair_date = models.DateTimeField('date published')
    repair_type = models.CharField(max_length=200)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'повреди'
