from django import forms

from News.models import Neighbourhood



class CreateNeighbourhoodForm(forms.Model):
    class Meta:
        model = Neighbourhood
        fields = ['name',]

class        