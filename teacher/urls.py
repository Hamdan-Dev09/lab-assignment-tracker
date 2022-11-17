from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('Course', views.course, name = 'course'),
    path('Course/Student', views.student, name = 'student-section'),
]