from django.shortcuts import render, redirect
from app.models import User

def index(request):

    context = {
        'users': User.objects.all()
    }
    for user in context['users']:
        print(user)

    return render(request, 'index.html', context)

def add (request):
     first_name = request.POST['firstName']
     last_name = request.POST['lastName']
     email = request.POST['email']
     age = request.POST['age']
     User.objects.create(first_name=first_name, last_name=last_name, email=email, age=age)
     return redirect('/')





