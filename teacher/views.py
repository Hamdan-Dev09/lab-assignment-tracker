from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            print("logged In")
            auth.login(request, user)
            return redirect('teacher')
        else:
            print("1 In")
            return redirect('/')
    else:
        return render(request, 'login.html')



def dashboard(request):
    return render(request, 'Dashboard.html')

def course(request):
    return render(request, 'Course.html')

def student(request):
    return render(request, 'student-section.html')