

from django.shortcuts import render,redirect
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Beneficiaires
from .forms import Ben
# Create your views here.
def index(request):
    return render(request, 'index.html',context={"date":datetime.today()})

def index2(request):
    return render(request,'index2.html')

def index3(request):
    if request.method=="POST":
        form = Ben(request.POST).save()
        return redirect('/inscription')
    else:
        form=Ben()

    return render(request,'index3.html',{'form':form})