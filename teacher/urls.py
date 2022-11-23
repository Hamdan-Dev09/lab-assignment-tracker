from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher', views.dashboard, name = 'teacher'),
    path('course/<str:slug>', views.course, name = 'course'),
    path('student/<str:faculty_no>', views.student, name = 'student'),
    path('check_week/<int:week_st_id>', views.check_week, name = 'check_week'),
    path('uncheck_week/<int:week_st_id>', views.uncheck_week, name = 'uncheck_week'),
]