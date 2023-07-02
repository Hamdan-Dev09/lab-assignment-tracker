from django.db import models
from accounts.models import CustomUser as User
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Degree(models.Model):
    degree_name = models.CharField(max_length=50)

    def __str__(self):
        return self.degree_name
    

class Course(models.Model):
    program = models.ForeignKey(Degree, on_delete=models.CASCADE)
    semester = models.IntegerField()
    lab_manual = models.FileField(upload_to='lab_manuals/',blank=True, null=True)
    code = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)

    def __str__(self):
        return self.title


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return str(self.user)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    faculty_no = models.CharField(max_length = 15)
    mentor = models.ForeignKey(Mentor, on_delete = models.PROTECT)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Week(models.Model):
    week_no = models.IntegerField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    lastDate = models.DateField(blank = True, null = True)

    def __str__(self):
        return str(self.week_no)


class WeekStatus(models.Model):
    week = models.ForeignKey(Week, on_delete = models.CASCADE)
    marks = models.IntegerField(blank=True, null=True,
        validators=[
            MinValueValidator(0, message='Value must be greater than or equal to 0.'),
            MaxValueValidator(10, message='Value must be less than or equal to 10.')
        ]
    )
    file = models.FileField(upload_to = 'uploads/', blank = True, null = True)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    submittedOn = models.DateField(blank = True, null = True)
    
    def __str__(self):
        return f"{self.student.name}-{self.week.week_no} week"
