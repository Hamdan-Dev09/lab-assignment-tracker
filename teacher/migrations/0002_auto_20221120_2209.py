# Generated by Django 2.2 on 2022-11-20 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='password',
        ),
        migrations.AddField(
            model_name='mentor',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
