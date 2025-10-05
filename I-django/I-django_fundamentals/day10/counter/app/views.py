from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    
    return render(request, 'app/index.html', {'counter': request.session.get('counter', 0), 'visit_count': get_visit_count(request.session)})

def counter(request: HttpRequest) -> HttpResponse:
    counter_value = request.session.get('counter', 0) + 1
    request.session['counter'] = counter_value
    return render(request, 'app/index.html', {'counter': counter_value, 'visit_count': get_visit_count(request.session)})

def reset(request: HttpRequest) -> HttpResponse:
    request.session['counter'] = 0
    return render(request, 'app/index.html', {'counter': 0, 'visit_count': get_visit_count(request.session)})

def destroy_session(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return render(request, 'app/index.html', {'counter': 0, 'visit_count': get_visit_count(request.session)})

def increment_by_2(request: HttpRequest) -> HttpResponse:
    counter_value = request.session.get('counter', 0) + 2
    request.session['counter'] = counter_value
    return render(request, 'app/index.html', {'counter': counter_value, 'visit_count': get_visit_count(request.session)})

def get_visit_count(session: Session) -> int:
    visit_count = session.get('visit_count', 0)
    visit_count += 1
    session['visit_count'] = visit_count
    return visit_count