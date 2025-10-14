from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('/shows/addNew')

def addNew(request):
    return render(request, 'index.html')

def addNewShow(request):
    if request.method == "POST":
        errors = TvShow.objects.add_show_validator(request.POST)

        if errors:
            for key, msg in errors.items():  
                messages.error(request, msg, extra_tags='addShow')
            return redirect('/shows/addNew')

        tvshow = add_show(request.POST)
        return redirect(f'/shows/{tvshow.id}')

    return redirect('/shows/addNew')  

def show(request, show_id):
    context = {
        'show': get_show(show_id)
    }
    return render(request, 'show.html', context)


def editShow(request, show_id):
    context = {
        'show': get_show(show_id)
    }
    return render(request, 'edit.html', context)


def editShows(request, show_id):
    if request.method == "POST":
        errors = TvShow.objects.add_show_validator(request.POST)
        if errors:
            for key, msg in errors.items():  
                messages.error(request, msg, extra_tags='editShow')
            return redirect(f'/shows/{show_id}/edit')
        tvshow = update_show(show_id, request.POST)
        return redirect(f'/shows/{tvshow.id}')
    return redirect(f'/shows/{show_id}')


def showAll(request):
    context = {
        'all_shows': TvShow.objects.all()
    }
    return render(request, 'shows.html', context)


def deleteShow(request, show_id):
    delete_show(show_id)
    return redirect('/shows')