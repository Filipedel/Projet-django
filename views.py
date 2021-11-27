
from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import bene,Cate,Prod
from django.db import IntegrityError
from django.contrib.auth import  authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Categorie,beneficiaire,Produit
from django.db.models import Avg, Count
# Create your views here.

#PAGE ACCUEIL
def index(request):
    return render(request, 'index.html',context={"date":datetime.today()})



#CONNEXION
def index2(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
             login(request, user)
             return redirect('bv')
        else:
            messages.warning(request,("Le mot de passe ou le nom d'utilisateur est incorrect:"))
            return redirect('index2')

    else:
        return render(request,'authenticate/index2.html')

def ciao(request):
    logout(request)
    messages.success(request,("Tu as été déconnecté(e)!"))
    return redirect('index')
#BENEFICIAIRE
@login_required(login_url='/connexion')
def benefi(request):
    benee = beneficiaire.objects.all().filter(valide=False)
    if request.method =="POST":
         return render(request, 'authenticate/Bene.html', {'bene': benee})


    else:
        print('ERROR')
        return render(request,'authenticate/Bene.html')

@login_required(login_url='/connexion')
def seebenefi(request,id):

    benee = beneficiaire.objects.filter(id=id)
    return render(request,'authenticate/SUCCESS.html',{'bene':benee})


def valbenef(request,id):
    val=beneficiaire.objects.all().filter(id=id)
    value=val.values('id')[0]['id']
    print (value)
    benefic = beneficiaire.objects.get(id=value)
    benefic.valide=True
    benefic.save()
    return redirect('beneto')

@login_required(login_url='/connexion')
def valide(request):
    all_entries = beneficiaire.objects.all().filter(valide=True)
    return render(request,'authenticate/validé.html',{'bene':all_entries})

def delbenef(request,id):
    benee = beneficiaire.objects.all().filter(id=id).delete()
    return redirect('beneto')

#LOGIN
@login_required(login_url='/connexion')
def Bienvenue(request):
    count = beneficiaire.objects.all().filter(valide=False).values("id").annotate(Count("id"))
    return render(request, 'authenticate/Login.html',{'for':count})



#FORMULAIRE INSCRIPTION
def index3(request):
    if request.method == "POST":
        form = bene(request.POST)
        if form.is_valid():
           benef=beneficiaire()
           benef.first_name = form.cleaned_data['first_name']
           benef.last_name = form.cleaned_data['last_name']
           benef.email =form.cleaned_data['email']
           benef.telephone = form.cleaned_data['telephone']
           benef.nbParts = form.cleaned_data['nbParts']
           benef.motMairie = form.cleaned_data['motMairie']
           benef.carteDonnee = form.cleaned_data['carteDonnee']
           benef.adresse =form.cleaned_data['adresse']
           benef.presenceDistribution=form.cleaned_data['presenceDistribution']
           benef.remarque=form.cleaned_data['remarque']
           benef.valide=False
           try:
               benef.save()
               messages.success(request, ("L'inscription s'est correctement déroulée"))
               redirect('index3')
           except IntegrityError:
               print("Erreur")
               redirect('index3')
        else:
            print("[LOG] invalid form!")
            print(form.errors)
            messages.warning(request, ("Veuillez réessayer"))
            redirect('index3')
    else:
        form = bene()
    all_entries = beneficiaire.objects.all()
    print(all_entries.values("first_name"))
    return render(request,'index3.html',{'form':bene})


#CATEGORIE
@login_required(login_url='/connexion')
def categorieadd(request):
    if request.method == "POST":
        categorieForm = Cate(request.POST)
        if categorieForm.is_valid():
            categorie = Categorie()
            categorie.nomcate = categorieForm.cleaned_data['nom']
            categorie.unite = 0
            try:
                categorie.save()
                messages.success(request, ("Vous avez bien ajouté la catégorie "+categorie.nomcate))
            except IntegrityError:
                redirect('cate')
        else:
            print("[LOG] invalid form!")
    else:
        categorieForm = Cate()
    all_entries = Categorie.objects.all()
    print(all_entries.values("nomcate"))
    return render(request, "authenticate/categorie.html", {'catform':all_entries,'catform2':Cate})

def delete(request, id):
    messages.success(request, ("Vous avez bien supprimé la catégorie "))
    Categorie.objects.all().filter(id=id).delete()
    return redirect('cate')



#Produits
@login_required(login_url='/connexion')
def produitadd(request):
    if request.method == 'POST':
        produitform =Prod(request.POST)
        if produitform.is_valid():
            produit=Produit()
            produit.nom=produitform.cleaned_data['nom']
            produit.categorie=produitform.cleaned_data['categorie']
            produit.unite_prod=produitform.cleaned_data['unite_prod']
            produit.seuil_alerte=produitform.cleaned_data['seuil_alerte']
            categorie = Categorie.objects.get(nomcate=produitform.cleaned_data['categorie'])
            categorie.unite = categorie.unite + 1
            categorie.save()
            produit.save()
            messages.success(request, ("Vous avez bien ajouté le produit "+produit.nom))
        else:
            print(produitform.errors)
            print (error)
    else:
        produitform=Prod()
    all_entries= Produit.objects.all()
    print(all_entries.values("nom"))
    return render(request, "authenticate/Produits.html", {"prodform": all_entries, "form":produitform})

def delete2(request, id):
    product = Produit.objects.all().filter(id=id)
    categorie_id = product.values('categorie')[0]['categorie']
    # Update categorie unite
    categorie = Categorie.objects.get(id=categorie_id)
    categorie.unite = categorie.unite - 1
    categorie.save()
    # delete product
    product.delete()
    return redirect('prod')