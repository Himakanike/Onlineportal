# Generated by Django 2.0.6 on 2018-06-24 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20180624_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='user',
            new_name='application',
        ),
        migrations.RemoveField(
            model_name='fee',
            name='application_no',
        ),
    ]
