from django.shortcuts import render
from .models import create_user, login_user
from django.shortcuts import redirect




def index(request):
    return render(request, 'index.html')

def register(request):
    create_user(request,request.POST)
    return redirect('/')

def login(request):
    login_user(request, request.POST, request.session)
    return redirect('/success')

def success(request):
    return render(request, 'succes.html')

def logout(request):
    request.session.flush()
    return redirect('/')
