from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher', views.dashboard, name = 'teacher'),
    path('student_dashboard', views.student_dashboard, name = 'student_dashboard'),
    path('course/<str:slug>', views.course, name = 'course'),
    path('student/<str:faculty_no>', views.student, name = 'student'),
    path('submit/<int:week_st_id>', views.submit_file, name = 'submit'),
    path('review/<int:week_st_id>', views.review, name = 'review'),
    path('check_week/<int:week_st_id>', views.check_week, name = 'check_week'),
    path('uncheck_week/<int:week_st_id>', views.uncheck_week, name = 'uncheck_week'),
]