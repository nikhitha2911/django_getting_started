# Generated by Django 3.1.5 on 2021-01-12 20:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='Start_time',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AddField(
            model_name='meeting',
            name='duration',
            field=models.IntegerField(default=1),
        ),
    ]
