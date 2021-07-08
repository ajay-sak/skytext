# Generated by Django 3.2.5 on 2021-07-07 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sst', '0007_auto_20210707_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdetails',
            name='test_paper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sst.testpaper', verbose_name='Test Paper'),
        ),
        migrations.AlterField(
            model_name='testdetails',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 20, 35, 59, 894980)),
        ),
        migrations.AlterField(
            model_name='testpaper',
            name='q_paper',
            field=models.FileField(upload_to='q_papers'),
        ),
    ]