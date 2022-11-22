from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teacher', views.dashboard, name = 'teacher'),
    path('course/<str:slug>', views.course, name = 'course'),
    path('student', views.student, name = 'student-section'),
]