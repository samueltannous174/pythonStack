from django.db import models
import bcrypt
import re
from datetime import datetime, timedelta
from django.utils import timezone


class RegisterManager(models.Manager):
    def Register_validator(self, postData):
        print(postData)
        errors = {}
        if User.objects.filter(email=postData['email']).exists():
            errors["email"] = "Email already exists"
        if len(postData['firstName']) < 2:
            errors["firstName"] = "First name should be at least 2 characters"
        if len(postData['lastName']) < 2:
            errors["lastName"] = "Last name should be at least 2 characters"
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', postData['email']):
            errors["email"] = "Email should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirmPassword']:
            errors["password"] = "Passwords do not match"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email']).first()

        if not user or not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors["login"] = "Invalid email or password"

        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"] = "Title should be at least 1 characters"
        if len(postData['desc']) < 5:
            errors["desc"] = "Description should be at least 5 characters"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= RegisterManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like  = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create( first_name=postData['firstName'], last_name=postData['lastName'], email=postData["email"], password=hashed_pw)

def login_user( postData):
    user = User.objects.get(email=postData['email'])
    return user

def get_all_books():
    return Book.objects.all()
def get_book(id):
    return Book.objects.get(id=id)
def delete_book(id):
    return Book.objects.get(id=id).delete()
def update_book(postData, id ):
    book = Book.objects.get(id=id)
    book.title = postData['title']
    book.desc = postData['desc']
    book.save()
    return book

def add_book(postData, user_id): 
    user = User.objects.get(id=user_id)
    book = Book.objects.create(title=postData['title'], desc=postData['desc'], uploaded_by=user)
    book.users_who_like.add(user)
    return book

def favorite_book(user_id, book_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.liked_books.add(book)
    return book
def unfavorite_book(user_id, book_id):
    user = User.objects.get(id=user_id)
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)
    return book