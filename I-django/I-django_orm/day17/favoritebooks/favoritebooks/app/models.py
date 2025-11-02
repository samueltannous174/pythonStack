from django.db import models
import bcrypt
import re
from datetime import datetime, timedelta

from datetime import datetime
from zoneinfo import ZoneInfo  



class RegisterManager(models.Manager):
    def Register_validator(self, postData):
        print(postData)
        errors = {}
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email already exists"
        if not postData['firstName'] or len(postData['firstName']) < 4:
            errors["firstName"] = "First name should be at least 2 characters"
        if not postData['lastName'] or len(postData['lastName']) < 4:
            errors["lastName"] = "Last name should be at least 2 characters"
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', postData['email']):
            errors["email"] = "Email should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirmPassword']:
            errors["password"] = "Passwords do not match"

        date_regex = r"^\d{4}\-(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[01])$"
        if not re.match(date_regex, postData['date']):
            errors["date"] = "Birth date must be in format YYYY-MM-DD"
        else:
            now = datetime.now(ZoneInfo('UTC'))  
            birthday = datetime.strptime(postData['date'], "%Y-%m-%d")
            birthday = birthday.replace(tzinfo=ZoneInfo('UTC'))
            age = now - birthday
            years = age.days // 365
            if years < 18: 
                errors["date"] = "User must be older than 18"

        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email']).first()

        if not user or not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors["login"] = "Invalid email or password"

        return errors
    

month_dict = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12
        }

class GameManager(models.Manager):

  def game_validator(self, postData):
    print(postData)
    errors = {}
    
    if not postData['game'] or len(postData['game']) < 2:
        errors["game"] = "Name should be at least 2 characters"
    
    date_format = r"^\d{1,2}-(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)-\d{4}$|^\d{1,2}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{4}$"
    if not re.match(date_format, postData['date']):
        errors["date"] = "Release date must be in format DD-MMM-YYYY with month in word"
    
    
    return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    date = models.DateField()
    avatar = models.CharField(max_length=255, default="https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegisterManager()

class Game (models.Model):
    name = models.CharField(max_length=255)
    genere = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="games", on_delete=models.CASCADE)
    players_liked = models.ManyToManyField(User, related_name="liked_games")
    objects = GameManager()

class Review(models.Model):
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name="reviews", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)







    
def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    print(postData['date'])
    return User.objects.create( first_name=postData['firstName'], last_name=postData['lastName'], email=postData["email"], password=hashed_pw, date=postData['date'], avatar=postData['avatar'])

def login_user( postData):
    user = User.objects.get(email=postData['email'])
    return user


def create_game(postData, user_id):
    user = User.objects.get(id=user_id)
    date = datetime.strptime(postData['date'], "%d-%b-%Y").date()
    print(date)
    return Game.objects.create(name=postData['game'], genere=postData['genere'], release_date=date, description=postData['desc'], user=user)


def get_all_games():
    return Game.objects.all()

def sort_games_by_genre():
    return Game.objects.all().order_by('genere')

def get_game(id):
    return Game.objects.get(id=id)

def get_who_likes_game(game_id):
    game = Game.objects.get(id=game_id)
    return game.players_liked.all()

def add_review(postData,user_id, game_id):
    user = User.objects.get(id=user_id)
    game = Game.objects.get(id=game_id)
    review = Review.objects.create(rating=postData['rating'], user=user, game=game)
    return review

def add_favorites(user_id, game_id):
    user = User.objects.get(id=user_id)
    game = Game.objects.get(id=game_id)
    game.players_liked.add(user)

def who_likes(user_id, game_id):
    user = User.objects.get(id=user_id)
    game = Game.objects.get(id=game_id)
    game.players_liked.all()


def update_game(postData, game_id):
    game = Game.objects.get(id=game_id)
    date = datetime.strptime(postData['date'], "%d-%b-%Y").date()
    game.game = postData['game']
    game.genere = postData['genere']
    game.release_date = date
    game.description = postData['description']
    game.save()


def delete_game(game_id):
    game = Game.objects.get(id=game_id)
    game.delete()