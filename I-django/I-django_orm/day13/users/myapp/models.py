from django.db import models
class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=25)
    street= models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="address" , on_delete= models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



