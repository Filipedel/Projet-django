from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('inscription', views.index3, name="index3"),
    path('connexion',views.index2,name="index2"),
    path('', views.index, name="index"),
    path('Bienvenue',views.Bienvenue,name="bv"),
    path('logout',views.ciao,name="ciao"),
    path('beneficiaire',views.benefi,name="beneto"),
    path('produits',views.produitadd,name="prod"),
    path('categorie',views.categorieadd,name="cate"),
    path('categorie/delete/<int:id>', views.delete, name='delete'),
    path('produits/delete/<int:id>', views.delete2, name='delete2'),
    path('beneficiaire/SUCCESS/<int:id>',views.seebenefi,name='see'),
    path('beneficiaire/SUCCESS/valide/<int:id>',views.valbenef,name='success'),
    path('beneficiaire/SUCCESS/delete/<int:id>', views.delbenef, name='supprime'),
    path('validation', views.valide, name='succeed'),
]