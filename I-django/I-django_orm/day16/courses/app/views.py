from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        "courses": all_courses(),
    }
    return render(request, 'index.html', context)

def addCourse(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if errors:
            for key, msg in errors.items():  
                messages.error(request, msg)
            return redirect('/')
        course = add_course(request.POST)
        messages.success(request, "Course added successfully!")
        return redirect('/')    
    return redirect('/')

def deleteCourse(request, course_id):
        request.session['course_id'] = course_id
        return render(request, 'destroy.html')

def destroyCourse(request):
    if request.method == 'POST':
        delete_course(request.session['course_id'])
        messages.success(request, "Course deleted successfully!")
    return redirect('/')
