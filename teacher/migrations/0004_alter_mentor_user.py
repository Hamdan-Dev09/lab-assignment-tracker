# Generated by Django 4.1.1 on 2022-11-22 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0003_alter_mentor_user_alter_student_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]