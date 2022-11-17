from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'Dashboard.html')

def course(request):
    return render(request, 'Course.html')

def student(request):
    return render(request, 'student-section.html')