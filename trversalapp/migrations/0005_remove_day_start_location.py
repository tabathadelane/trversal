# Generated by Django 2.2.1 on 2019-06-11 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trversalapp', '0004_auto_20190611_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='start_location',
        ),
    ]
