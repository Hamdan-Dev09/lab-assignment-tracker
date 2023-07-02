from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mentor,Course, WeekStatus, Week, Student
from django.utils import timezone
from django.db.models import Sum


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            print(request.user.is_teacher)
            return redirect('teacher')
        else:
            return redirect('student_dashboard')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_teacher:
        return redirect('student_dashboard')
    
    color_arr = ["bg1","bg2","bg3","bg4","bg5","bg6","bg7","bg8","bg9"]
    mentor_obj = Mentor.objects.get(user=request.user)
    courses = mentor_obj.courses.all()
    for course in courses:
        course.color = color_arr.pop()
    return render(request, 'Dashboard.html', {'courses': courses})

@login_required(login_url='login')
def student_dashboard(request):
    if request.user.is_teacher:
        return redirect('teacher')
    
    # Student Details
    student = Student.objects.get(user=request.user)
    
    
    # Marks Details
    week_list = WeekStatus.objects.filter(student__user=request.user)
    marks_sum = week_list.aggregate(Sum('marks'))
    finished_weeks_in_class = WeekStatus.objects.filter(week__lastDate__lte=timezone.now().date(), student__user=request.user).values_list('pk', flat=True)
    weeks_completed_other_than_finished = WeekStatus.objects.filter(marks__isnull=False, student__user=request.user).exclude(pk__in=finished_weeks_in_class).count()
    out_of_marks = weeks_completed_other_than_finished * 10 + finished_weeks_in_class.count() * 10
    print(marks_sum['marks__sum'])
    print(out_of_marks)
    
    
    # Show all weeks
    for week_st in week_list:
        if week_st.submittedOn is None:
            week_st.status = 'Pending'
        elif week_st.submittedOn <= week_st.week.lastDate:
            week_st.status = 'Submitted'
        else:
            week_st.status = 'Late'
            
    print("***")
    for week_st in week_list:
        print(week_st.__dict__)
    
    return render(request, 'student_dashboard.html', {'week_list': week_list, 'student': student, 'marks_sum': marks_sum['marks__sum'], 'out_of_marks': out_of_marks})

@login_required(login_url='login')
def course(request, slug):
    if not request.user.is_teacher:
        return redirect('student_dashboard')
        
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
    if not request.user.is_teacher:
        return redirect('student_dashboard')
    
    
    week_list = WeekStatus.objects.filter(student__faculty_no=faculty_no)
    marks_sum = week_list.aggregate(Sum('marks'))
    finished_weeks_in_class = WeekStatus.objects.filter(week__lastDate__lte=timezone.now().date(), student__faculty_no=faculty_no).values_list('pk', flat=True)
    weeks_completed_other_than_finished = WeekStatus.objects.filter(marks__isnull=False, student__faculty_no=faculty_no).exclude(pk__in=finished_weeks_in_class).count()
    out_of_marks = weeks_completed_other_than_finished * 10 + finished_weeks_in_class.count() * 10
    print(marks_sum['marks__sum'])
    print(out_of_marks)
    
    student = Student.objects.get(faculty_no=faculty_no)
    week_list = student.weekstatus_set.all()
    for week_st in week_list:
        if week_st.submittedOn is None:
            week_st.status = 'Pending'
        elif week_st.submittedOn <= week_st.week.lastDate:
            week_st.status = 'Submitted'
        else:
            week_st.status = 'Late'
    return render(request, 'student-section.html', {'student': student, 'week_list': week_list, 'marks_sum': marks_sum['marks__sum'], 'out_of_marks': out_of_marks})

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


@login_required(login_url='login')
def submit_file(request, week_st_id):
    if request.method == 'POST':
        week_st = WeekStatus.objects.get(id=week_st_id)
        week_st.submittedOn = timezone.now().date()
        week_st.file = request.FILES['file']
        week_st.save()
        return redirect('student', faculty_no=week_st.student.faculty_no)
    else:
        # Handle GET request or render an error page if necessary
        # Here, you can return an HttpResponse or render a template
        pass
    
    
@login_required(login_url='login')
def review(request, week_st_id):
    if not request.user.is_teacher:
        return redirect('student_dashboard')
    
    if request.method == 'POST':
        week_st = WeekStatus.objects.get(id=week_st_id)
        week_st.marks = request.POST['marks']
        week_st.save()
        return redirect('student', faculty_no=week_st.student.faculty_no)