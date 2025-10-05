from django.shortcuts import render
import random

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def submitted(request):
    if request.session.get('guess') is None:
        request.session['guess'] = random.randint(1, 100)
        print(f"Secret number: {request.session['guess']}")  

    if request.session.get('count') is None:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    guess = int(request.POST.get('guess', 0))
    target = request.session['guess']
    count = request.session['count']

    if guess < target:
        message = f"Too low! Current count: {count}"
    elif guess > target:
        message = f"Too high! Current count: {count}"
    else:
        message = f"You won! Total guesses: {count}"

    return render(request, 'index.html', {
        'message': message,
        'guess': guess,
        'target': target,

    })

def reset(request):
    request.session.flush()
    return render(request, 'index.html')
