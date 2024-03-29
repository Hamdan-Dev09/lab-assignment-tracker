# Generated by Django 4.1.3 on 2023-07-02 01:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0002_alter_student_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="weekstatus",
            name="file",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="weekstatus",
            name="marks",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="Value must be greater than or equal to 0."
                    ),
                    django.core.validators.MaxValueValidator(
                        10, message="Value must be less than or equal to 10."
                    ),
                ],
            ),
        ),
    ]
