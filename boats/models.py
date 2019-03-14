from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Boat(models.Model):

    id = models.AutoField(primary_key=True)#
    #d = models.AutoField(primary_key=True)#models.IntegerField(max_length=11)
    name = models.CharField(max_length=40)
    #type = models.CharField(max_length=10)
    owner_id = models.IntegerField()
    #date_made = models.DateTimeField(default=datetime.date.today())
    rental_price = models.FloatField()

    #def __str__(self):
    #    return str(self.id+self.name+self.owner_id+self.rental_price)#self.type+self.owner_id+self.date_made+self.rental_price)

    class Meta:
        verbose_name_plural = 'лодки'