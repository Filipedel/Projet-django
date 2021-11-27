
from django.db import models
from django.db.models.fields import CharField, IntegerField ,EmailField,BooleanField,DateField
from django.db.models.fields.files import ImageField

class Categorie(models.Model):
    nomcate = CharField(max_length=30, unique=True)
    unite = IntegerField()
    def __str__(self):
        return self.nomcate

class Produit(models.Model):
    nom=CharField(max_length=30,unique=True)
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    unite_prod=models.IntegerField()
    seuil_alerte=models.IntegerField()


class beneficiaire(models.Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    email =EmailField()
    telephone =CharField(max_length=10)
    adresse = EmailField()
    nbParts = IntegerField()
    motMairie =BooleanField()
    carteDonnee =BooleanField()
    presenceDistribution =DateField()
    remarque = CharField(max_length=200,null=True)
    valide=BooleanField()

