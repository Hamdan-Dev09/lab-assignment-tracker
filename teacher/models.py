from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Course(models.Model):
    class_name = models.CharField(max_length = 50)
    semester = models.IntegerField()
    lab_code = models.CharField(max_length = 50)
    lab_title = models.CharField(max_length = 50)

    def __str__(self):
        return self.class_name



class Mentor(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    password = models.CharField(max_length = 80)
    image = models.ImageField(blank = True, null = True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length = 50)
    faculty_no = models.CharField(max_length = 15)
    mentor = models.ForeignKey(Mentor, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Week(models.Model):
    # week_id = models.CharField(max_length = 10)
    week_no = models.IntegerField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    lastDate = models.DateField(blank = True, null = True)


    def __str__(self):
        return self.week_no


class WeekStatus(models.Model):
    week = models.ForeignKey(Week, on_delete = models.CASCADE)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    submittedOn = models.DateField(blank = True, null = True)
    
     
