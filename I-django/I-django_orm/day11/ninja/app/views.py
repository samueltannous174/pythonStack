from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    
    return render(request, 'forms.html')

def submitted(request):
    print("hello")
    value = request.POST.get("form")

    if "gold" not in request.session:
        request.session["gold"] = 0
    if "activity" not in request.session:
        request.session["activity"] = []

    random_gold = 0

    if value == "farm":
        random_gold = random.randint(10, 20)
    elif value == "house":
        random_gold = random.randint(10, 20)
    elif value == "cave":
        random_gold = random.randint(10, 20)
    elif value == "quest":
        random_gold = random.randint(0, 50)
        message_type = random.choice(["takes", "earns"])
        message = f"{message_type.capitalize()} {random_gold} gold from the {value}!"


    if value == "quest":
        if message_type == "takes":
            request.session["gold"] -= random_gold
            request.session["activity"].append(message)
            return redirect("/")
        
    request.session["gold"] += random_gold

    message = f"Earned {random_gold} gold from the {value}!"
    request.session["activity"].append(message)

    print("new gold:", request.session["gold"])
    return redirect("/")