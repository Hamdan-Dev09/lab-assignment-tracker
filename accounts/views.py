from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from teacher.selectors import get_student_by_faculty_no
from teacher.utils import redirect_to_dashboard


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('teacher')

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('teacher' if user.is_teacher else 'student_dashboard')
        else:
            messages.info(request,'Invalid Credentials !')
            return redirect('login')
    else:
        return render(request, 'login.html')
     

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out')
    return redirect('login')