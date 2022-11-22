from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mentor,Course

def home(request):
    if request.user.is_authenticated:
        return redirect('teacher')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    mentor_obj = Mentor.objects.get(user=request.user)
    courses = mentor_obj.courses.all()
    return render(request, 'Dashboard.html', {'courses': courses})

def course(request, slug):
    course_obj = Course.objects.get(code=slug)
    students = course_obj.student_set.filter(mentor__user=request.user)
    return render(request, 'Course.html', {'course': course_obj, 'students': students})

def student(request):
    return render(request, 'student-section.html')