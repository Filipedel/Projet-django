from django import forms
from .models import Produit
from django.forms import ModelForm


class bene(forms.Form):
        id=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
        first_name = forms.CharField(label='Prénom', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
        last_name = forms.CharField(label='Nom de famille', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
        email = forms.EmailField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
        telephone = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'0909090909'}))
        adresse = forms.EmailField(required=False,max_length=30,widget=forms.EmailInput(attrs={'class':'form-control'}))
        nbParts = forms.IntegerField(required=False,label='Age',min_value=0,max_value=120,widget=forms.NumberInput(attrs={'class':'form-control'}))
        motMairie = forms.BooleanField(required=False,widget=forms.NullBooleanSelect(attrs={'class':'form-select'}))
        carteDonnee = forms.BooleanField(required=False,widget=forms.NullBooleanSelect(attrs={'class':'form-select'}))
        presenceDistribution = forms.DateField(widget=forms.SelectDateWidget())
        remarque = forms.CharField(max_length=200,required=False,widget=forms.Textarea())
class Cate(forms.Form):

        nom = forms.CharField(label='nom', widget=forms.TextInput(attrs={'class': 'form'}))

class Prod(ModelForm):
        class Meta:
                model=Produit
                fields=['nom','categorie','unite_prod','seuil_alerte']
