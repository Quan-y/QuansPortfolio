# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-01-29 23:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 23, 10, 38, 409328, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 29, 23, 10, 38, 408722, tzinfo=utc)),
        ),
    ]
