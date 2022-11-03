from django.contrib import admin
from .models import Course, Week,WeekStatus,Mentor,Student

# Register your models here.
admin.site.register(Course)
admin.site.register(Week)
admin.site.register(WeekStatus)
admin.site.register(Mentor)
admin.site.register(Student)
