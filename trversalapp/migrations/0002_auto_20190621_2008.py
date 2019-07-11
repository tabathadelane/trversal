# Generated by Django 2.2.2 on 2019-06-22 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trversalapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='trip_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='trversalapp.Trip'),
        ),
        migrations.AlterField(
            model_name='location',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locs', to='trversalapp.Day'),
        ),
    ]