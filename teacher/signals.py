from django.dispatch import receiver
from django.contrib.auth.models import User
from teacher.models import Mentor, Week, Student
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_mentor(sender,created, instance,**kwargs):
    if created:
        Mentor.objects.create(user=instance)
        

@receiver(post_save, sender=Week)
def create_week_status(sender,created, instance,**kwargs):
    if created:
        for student in instance.course.student_set.all():
            student.weekstatus_set.create(week=instance)
    
@receiver(post_save, sender=Student)
def create_week_status_for_new_student(sender,created, instance,**kwargs):
    if created:
        for week in instance.course.week_set.all():
            instance.weekstatus_set.create(week=week)
# @receiver(post_save, sender=User)
# def update_mentor(sender,created, instance,**kwargs):
#     if created == False:
#         instance.profile.save()
        

