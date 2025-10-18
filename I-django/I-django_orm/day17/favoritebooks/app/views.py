from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib import messages



# Create your views here.

def index(request):
    return render(request,'auth.html')

