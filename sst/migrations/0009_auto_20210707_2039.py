# Generated by Django 3.2.5 on 2021-07-07 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sst', '0008_auto_20210707_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testpaper',
            options={'ordering': ['-paper_name']},
        ),
        migrations.AlterField(
            model_name='testdetails',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 20, 39, 47, 917078)),
        ),
    ]