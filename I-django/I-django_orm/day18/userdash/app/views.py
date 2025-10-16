from django.shortcuts import render
from django.contrib import messages
from .models import *
from django.shortcuts import redirect


# Create your views here.


def index(request):
    return render(request, 'login.html')

def registerShow(request):
    return render(request, 'register.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.Register_validator(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg, extra_tags='register')
            return redirect('/')
        
        create_user(request.POST)

        messages.success(request, "Registration successful! You can now log in.", extra_tags='register')
        return redirect('/')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg, extra_tags='login')
            return redirect('/')
        print(request.POST)
        user = login_user(request.POST)
        print(user)
        request.session['name'] = user.first_name
        messages.success(request, f"Welcome back, {user.first_name}!", extra_tags='login')
        return redirect('/success')

    return redirect('/')



def success(request):
    if 'name' not in request.session:
        messages.error(request, "Please log in first.", extra_tags='login')
        return redirect('/')
    return render(request, 'succes.html')


def logout(request):
    request.session.flush()
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "You have logged out successfully.", extra_tags='login')
    return redirect('/')


def allUsers(request):
    context = {
        'users': get_all_users()
    }
    return render(request, 'allUsers.html', context)


def editUser(request, id):
    edit_user(request.POST, id)

    return redirect('/allUsers')

def editShow(request):
    return render(request, 'editUser.html')