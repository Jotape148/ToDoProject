# Generated by Django 5.2.1 on 2025-06-18 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='isCompleted',
            new_name='completed',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
    ]
