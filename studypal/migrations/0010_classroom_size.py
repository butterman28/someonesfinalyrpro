# Generated by Django 5.0.1 on 2024-03-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("studypal", "0009_classroom_classparticipants"),
    ]

    operations = [
        migrations.AddField(
            model_name="classroom",
            name="size",
            field=models.IntegerField(default=0),
        ),
    ]
