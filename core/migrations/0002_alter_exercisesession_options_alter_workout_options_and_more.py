# Generated by Django 5.0.1 on 2024-02-24 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercisesession',
            options={'ordering': ['routine']},
        ),
        migrations.AlterModelOptions(
            name='workout',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='routine',
            name='exercises',
        ),
    ]