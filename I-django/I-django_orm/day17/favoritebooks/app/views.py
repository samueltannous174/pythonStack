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
        
        user = create_user(request.POST)
        request.session['id'] = user.id
        request.session['name'] = user.first_name
        request.session['avatar'] = user.avatar
        messages.success(request, "Registration successful! You can now log in.", extra_tags='register')
        return redirect('/success')
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
        request.session['avatar'] = user.avatar
        messages.success(request, f"Welcome back, {user.first_name}!", extra_tags='login')
        return redirect('/success')

    return redirect('/')

def success(request):
    if 'id' not in request.session:
        messages.error(request, "Please log in first.", extra_tags='login')
        return redirect('/')

    context = {
        'all_games': get_all_games(),
    }
    

    return render(request, 'allGames.html', context)

def sortByGenere(request):
    context = {
        'all_games': sort_games_by_genre(),
    }
    return render(request, 'allGames.html', context)

def logout(request):
    request.session.flush()
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "You have logged out successfully.", extra_tags='login')
    return redirect('/')


def addGame(request):
    if request.method == 'POST':
        errors = Game.objects.game_validator(request.POST)
        if errors:
            for msg in errors.values():
                messages.error(request, msg)
            return redirect('/success')
        create_game(request.POST, request.session['id'])
        return redirect('/success')
    return redirect('/success')


def showGame(request, game_id):
    context = {
        'game': get_game(game_id)
    }
    return render(request, 'showGame.html', context)

def addToFavorites(request, game_id):
    add_review( request.POST,request.session['id'], game_id)
    add_favorites(request.session['id'], game_id)   
    return redirect(f'/game/{game_id}')

def get_who_likes_game(request, game_id):
    context = {
        'who_likes_game': get_who_likes_game(game_id)
    }
    return render(request, 'showGame.html', context)




def updateGame(request, game_id):
    print(game_id)
    request.session['game_id'] = game_id
    game = Game.objects.get(id=game_id)
    context = {
        'game': game
    }
    return render(request, 'edit.html', context)

def updateGame2(request, game_id):
        print(request.POST)
        if request.method == 'POST':
            errors = Game.objects.game_validator(request.POST)
            if errors:
                for msg in errors.values():
                    messages.error(request, msg)
                return redirect(f'/game/{game_id}')
            update_game(request.POST, game_id)
        
        return redirect(f'/game/{game_id}')
        
        
        

def deleteGame(request, game_id):
    delete_game(game_id)
    return redirect('/success')