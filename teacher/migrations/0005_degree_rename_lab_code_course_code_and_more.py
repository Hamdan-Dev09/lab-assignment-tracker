# Generated by Django 4.1.1 on 2022-11-22 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_alter_mentor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='lab_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='lab_title',
            new_name='title',
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacher.degree'),
            preserve_default=False,
        ),
    ]
