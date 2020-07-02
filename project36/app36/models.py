from django.db import models

# Create your models here.
class vistara(models.Model):
    f_no=models.CharField(max_length=40)
    f_origin=models.CharField(max_length=40)
    f_destPlace=models.CharField(max_length=40)
    f_destTime=models.CharField(max_length=50)
class makemytrip(models.Model):
    f_name=models.CharField(max_length=50)
    f_number=models.CharField(max_length=50)
    f_departuretime= models.CharField(max_length=50)
    f_departureplace = models.CharField(max_length=50)
    f_arrivaltime=models.CharField(max_length=50)
    f_arrivalplace=models.CharField(max_length=50)
class yatra(models.Model):
    f_name=models.CharField(max_length=50)
    f_number = models.CharField(max_length=50)
    f_departuretime = models.CharField(max_length=50)
    f_arrivaltime=models.CharField(max_length=50)