# Generated by Django 3.2.5 on 2021-07-07 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210707_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content_tag',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 14, 13, 11, 761429)),
        ),
    ]
