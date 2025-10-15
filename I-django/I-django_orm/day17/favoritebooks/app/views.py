from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib import messages



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
    if 'id' not in request.session:
        messages.error(request, "Please log in first.", extra_tags='login')
        return redirect('/')
    
    context={
    "allBooks":get_all_books()
    }
    return render(request, 'allBooks.html', context)


def logout(request):
    request.session.flush()
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "You have logged out successfully.", extra_tags='login')
    return redirect('/')

def addBook(request):
    if request.method == 'POST':
        add_book(request.POST, request.session['id'])
        return redirect('/success')
    return redirect('/success')


def viewBook(request,book_id):
    context = {
        "book":get_book(book_id),
    }
    return render(request, 'book.html', context)

def deleteBook(request,book_id):
    if request.method == 'POST':
        delete_book(book_id)
        return redirect('/success')
    return redirect('/success')

def updateBook(request,book_id):
    print(request.POST, book_id)
    update_book(request.POST, book_id)
 
    return redirect(f'/books/{book_id}')

def unfavoriteBook(request,user_id,book_id):
    if request.method == 'POST':
        unfavorite_book(user_id,book_id)
        redirect('/success')
    return redirect('/success')

def favoriteBook(request,user_id,book_id):
    if request.method == 'POST':
        favorite_book(user_id,book_id)
        print(request.POST)
        print(user_id,book_id)
        return redirect(f'/books/{book_id}')
    return redirect('/success')