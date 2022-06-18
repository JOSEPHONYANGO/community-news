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

class Neighborhood(models.Model):
    hood_image =  CloudinaryField('image', null=True)
    name = models.CharField(max_length=100)
    hood_description = models.TextField(max_length=1000, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def create_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_neighborhood(cls, id):
        cls.objects.filter(id=id).update()
    

    @classmethod
    def search_by_name(cls, search_term):
        hood = cls.objects.filter(name__icontains=search_term)
        return hood

    # find neighbourhood by id
    @classmethod
    def find_neigborhood(cls, id):
        hood = cls.objects.get(id=id)
        return hood

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username =  models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    neighbourhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    mobile_number = models.IntegerField(blank=True, null=True)
    email =  models.CharField(max_length=60) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)    

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()       



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
