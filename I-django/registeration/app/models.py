from django.db import models
import re
from django.contrib import messages
import bcrypt
# Create your models here.
class RegisterManager(models.Manager):
    def basic_validator(self, postData):
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
  
      

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= RegisterManager()

    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




def create_user(request,postData):
    errors = User.objects.basic_validator(postData) 
    # print("hello") 
    # print(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(first_name=postData['firstName'], last_name=postData['lastName'], email=postData["email"], password=hashed_pw)
    return user




def login_user(request, postData, session):
    errors = {}
    user = User.objects.get(email=postData['email'])

    if not user:
        errors['email'] = "Email does not exist"
        messages.error(request, errors['email'])
        return None
    
    if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
        errors['password'] = "Password is incorrect"
        messages.error(request, errors['password'])
        return None
    
    print(user.first_name)
    session['name'] = user.first_name   

    return user


 












