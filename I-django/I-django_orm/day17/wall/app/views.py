from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib import messages

from datetime import timedelta


# Create your views here.

def index(request):
    return render(request,'auth.html')




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

        request.session['id'] = user.id
        request.session['name'] = user.first_name
        messages.success(request, f"Welcome back, {user.first_name}!", extra_tags='login')
        return redirect('/success')

    return redirect('/')



def success(request):
    if 'name' not in request.session:
        messages.error(request, "Please log in first.", extra_tags='login')
        return redirect('/')
    context={
        'user_messages':get_all_messages()
    }
    return render(request, 'index.html', context)


def logout(request):
    request.session.flush()
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "You have logged out successfully.", extra_tags='login')
    return redirect('/')

def addMessage(request):
    if request.method == 'POST':
        add_message(request.POST, request.session['id'])
    return redirect('/success')
def addComment(request,message_id):
    if request.method == 'POST':
        add_comment(request.POST, request.session['id'], message_id)
    return redirect('/success')

def deleteMessage(request,message_id):
    if request.method == 'POST':


        
        delete_message(message_id)
        
    return redirect('/success')