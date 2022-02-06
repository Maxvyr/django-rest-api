from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=450)
    price=models.FloatField(default=0)