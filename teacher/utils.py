from django.shortcuts import redirect

def redirect_to_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teacher')
        else:
            return redirect('student_dashboard')