from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # save location
    def save_category(self):
        self.save()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # save location
    def save_location(self):
        self.save()

    def __str__(self):
        return self.name        




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
