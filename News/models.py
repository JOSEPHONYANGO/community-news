from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.IntegerField(max_length=50)
    admin = models.ForeignKey(admin,on_delete=models.CASCADE)

class User (models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(max_length=100) 
    Neighbourhood = models.ForeignKey(Neighbourhood)
    Email = models.EmailField(max_length=100)

class Business(models.Model):
    Business_name = models.CharField(max_length=100)
    User = models.ForeignKey(Business,on_delete=models.CASCADE)
    Neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    Business_email = models.EmailField(max_length=100)       
