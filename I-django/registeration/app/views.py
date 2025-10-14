from django.shortcuts import render, redirect
from django.contrib import messages
from .models import create_user, login_user, User

def index(request):
    request.session.flush()
    return render(request, 'index.html')


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

        user = login_user(request.POST)

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
