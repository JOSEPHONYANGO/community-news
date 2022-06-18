from django import forms

from News.models import Neighbourhood



class CreateNeighbourhoodForm(forms.Model):
    class Meta:
        model = Neighbourhood
        fields = ['name',]

class DeleteNeighbourhoodForm(forms.Model):
    class Meta:
        model = Neighbourhood
        fields = ['name']

class FindNeighbourhoodForm(forms.Model):
    class Meta:
        model =         

class UpdateNeighbourhoodForm(forms.Model):
    class Meta:
        model = 

class UpdateOccupants(forms.Model):
    class Meta:
        model =         