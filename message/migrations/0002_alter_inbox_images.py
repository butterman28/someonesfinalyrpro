# Generated by Django 5.0.1 on 2024-03-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("message", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inbox",
            name="images",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to="message_pics/"
            ),
        ),
    ]
