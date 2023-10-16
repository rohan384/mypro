from django.db import models

# Create your models here.
class Bustime(models.Model):
    bus_name=models.CharField(max_length=30,verbose_name='Bus Name')
    b_from=models.CharField(max_length=15,verbose_name='From')
    departure=models.TimeField(verbose_name='Departure')
    to=models.CharField(max_length=15,verbose_name='To')
    arrival=models.TimeField(verbose_name='Arrival')

# class Busroute(models.Model):
#     stop=models.TextField(verbose_name='Stop')
    # depart=models.TimeField(verbose_name='Depart')

class product(models.Model):
    name=models.CharField(max_length=20)