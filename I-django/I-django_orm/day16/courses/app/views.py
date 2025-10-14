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
                messages.error(request, msg, extra_tags='addCourse')
            return redirect('/')
        try:
            course = add_course(request.POST)
            messages.success(request, "Course added successfully!", extra_tags='addCourse')
            return redirect('/')    
        except Exception as e:
            messages.error(request, f"Error creating course: {str(e)}", extra_tags='addCourse')
            return redirect('/')
    return redirect('/')

def deleteCourse(request, course_id):
    try :
        course = delete_course(course_id)
        messages.success(request, "Course deleted successfully!", extra_tags='deleteCourse')
        
    except Exception as e:
        messages.error(request, f"Error deleting course: {str(e)}", extra_tags='deleteCourse')
        return redirect('/')
    return redirect('/')