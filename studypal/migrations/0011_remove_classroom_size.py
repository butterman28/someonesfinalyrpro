# Generated by Django 5.0.1 on 2024-03-06 16:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("studypal", "0010_classroom_size"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="classroom",
            name="size",
        ),
    ]