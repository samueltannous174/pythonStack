from django.shortcuts import render, HttpResponse, redirect
from .models import *



def index(request):

    context = {
        "dojos": Dojo.objects.all()
    }


    return render(request, 'index.html', context)


def addNinja(request):
    create_ninja(request)
    
    return redirect("/")


def addDojo(request):
    create_dojo(request)

    return redirect("/")
