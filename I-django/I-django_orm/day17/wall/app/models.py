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
        if not user:
            errors["email"] = "Email not found"
        elif not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors["password"] = "Invalid password"
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



class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.message}"

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.comment}"




def add_comment(data, user_id, message_id):
    message=Message.objects.get(id=message_id)
    user = User.objects.get(id=user_id)
    comment = Comment.objects.create(comment=data['comment'], message=message, user=user)
    return comment

def add_message(data, user_id):
    user = User.objects.get(id=user_id)
    message = Message.objects.create(message=data['message'], user=user)
    return message
def get_all_messages():
    messages = Message.objects.all().order_by('-created_at')
    return messages

def create_user(postData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    return User.objects.create( first_name=postData['firstName'], last_name=postData['lastName'], email=postData["email"], password=hashed_pw)

def login_user( postData):
    user = User.objects.get(email=postData['email'])
    return user

def delete_message(message_id):
    message = Message.objects.get(id=message_id)
    time_limit = timezone.now() - timedelta(minutes=10)
        
    print(f"Current time: {timezone.now()}")
    print(f"Message created at: {message.created_at}")
    print(f"Time limit: {time_limit}")
        
    if message.created_at > time_limit:
            message.delete()
    return None


