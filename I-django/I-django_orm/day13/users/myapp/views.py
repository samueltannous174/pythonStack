from django.shortcuts import render
from myapp.models import User
# Create your views here.

def index(request):
    print("hello")
    context ={
        "users" : User.objects.all() }
        
    
    return render(request, 'index.html', context)