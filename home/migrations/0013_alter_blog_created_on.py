# Generated by Django 3.2.5 on 2021-07-08 09:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_blog_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 14, 56, 32, 445774)),
        ),
    ]
