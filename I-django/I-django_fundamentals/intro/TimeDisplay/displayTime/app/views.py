from django.utils import timezone
from django.shortcuts import render

def index(request):
    context = {
        'date': timezone.now().strftime("%Y-%m-%d"),
        'clock': timezone.now().strftime("%H:%M:%S %Z")
    }
    print(context)

    return render(request, 'app/index.html', context)