# Generated by Django 4.2.7 on 2023-11-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_api', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]