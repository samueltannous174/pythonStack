from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')

def counter(request):
    counter_value = request.session.get('counter', 0) + 1
    request.session['counter'] = counter_value
    return render(request, 'app/index.html', {'counter': counter_value})

def reset(request):
    request.session['counter'] = 0
    return render(request, 'app/index.html', {'counter': 0})





