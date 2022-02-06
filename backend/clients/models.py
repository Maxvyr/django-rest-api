from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    age=models.FloatField(default=0)
    sexe= models.IntegerField(default=0)
    