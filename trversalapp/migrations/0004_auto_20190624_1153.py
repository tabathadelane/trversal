# Generated by Django 2.2.2 on 2019-06-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trversalapp', '0003_auto_20190624_1033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='geo',
            new_name='g_lat',
        ),
        migrations.AddField(
            model_name='location',
            name='g_lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
