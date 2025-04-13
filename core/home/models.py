from django.db import models
# from home.models import *
# CRUD  

# Create your models here.
class Student(models.Model):
    # id = models.AutoField() --> this is automaticaly taken by django and it is also a primary key
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null = True, blank= True)
   

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50 )

    def __str__(self) -> str: 
        return self.car_name