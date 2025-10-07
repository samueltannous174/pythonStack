
from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=5)
    desc = models.TextField(default="old dojo")
  

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)






def create_dojo(request):
    Dojo.objects.create(name=request.POST["dojo"], city=request.POST["city"], state=request.POST["state"])


def create_ninja(request):
    print(request.POST)
    Ninja.objects.create(first_name=request.POST["name"], last_name=request.POST["last"], dojo=Dojo.objects.get(id=request.POST["dojo"]))