from django.dispatch import receiver
from django.contrib.auth.models import User
from teacher.models import Mentor
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_mentor(sender,created, instance,**kwargs):
    if created:
        Mentor.objects.create(user=instance)
        

# @receiver(post_save, sender=User)
# def update_mentor(sender,created, instance,**kwargs):
#     if created == False:
#         instance.profile.save()
        

