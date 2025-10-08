from django.shortcuts import render, redirect
from .models import *



def index(request):

    context = {
        "books": get_all_books(),
    }
    return render(request, 'index.html', context)

def addBook(request):
    print(request.POST)
    title = request.POST['title']
    desc = request.POST['desc']
    add_book(title,desc)
    return redirect('/')

def viewBook(request,book_id):
    context = {
        "book": get_book(book_id),
        "authors": get_book_authors(book_id),
        "allAuthors": get_all_authors()
    }
    return render(request, 'book.html', context)

def addAuthorToBook(request,book_id):
    author_id = request.POST["author_id"]
    add_author_to_book(author_id,book_id)
    return redirect(f'/books/{book_id}')    