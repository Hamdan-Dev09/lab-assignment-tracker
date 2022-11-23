from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mentor,Course, WeekStatus, Week, Student
from django.utils import timezone


def home(request):
    if request.user.is_authenticated:
        return redirect('teacher')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    color_arr = ["bg1","bg2","bg3","bg4","bg5","bg6","bg7","bg8","bg9"]
    mentor_obj = Mentor.objects.get(user=request.user)
    courses = mentor_obj.courses.all()
    for course in courses:
        course.color = color_arr.pop()
    return render(request, 'Dashboard.html', {'courses': courses})

@login_required(login_url='login')
def course(request, slug):
    course_obj = Course.objects.get(code=slug)
    students = course_obj.student_set.filter(mentor__user=request.user).prefetch_related('weekstatus_set')
    for student in students:
        student.completed_till = student.weekstatus_set.filter(submittedOn__isnull=False).count()

    weeks = Week.objects.filter(course=course_obj)
    for week in weeks:
        today_date = timezone.now().date()
        week.completed = today_date >= week.lastDate
    return render(request, 'Course.html', {'course': course_obj, 'students': students, 'weeks': weeks})

@login_required(login_url='login')
def student(request, faculty_no):
    student = Student.objects.get(faculty_no=faculty_no)
    week_list = student.weekstatus_set.all()
    for week_st in week_list:
        if week_st.submittedOn is None:
            week_st.status = 'Pending'
        elif week_st.submittedOn <= week_st.week.lastDate:
            week_st.status = 'Submitted'
        else:
            week_st.status = 'Late'
    return render(request, 'student-section.html', {'student': student, 'week_list': week_list})

@login_required(login_url='login')
def check_week(request, week_st_id):
    week_st = WeekStatus.objects.get(id=week_st_id)
    week_st.submittedOn = timezone.now().date()
    week_st.save()
    return redirect('student', faculty_no=week_st.student.faculty_no)

@login_required(login_url='login')
def uncheck_week(request, week_st_id):
    week_st = WeekStatus.objects.get(id=week_st_id)
    week_st.submittedOn = None
    week_st.save()
    return redirect('student', faculty_no=week_st.student.faculty_no)