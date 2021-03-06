# Generated by Django 3.1.5 on 2021-01-07 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210106_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(upload_to='music'),
        ),
        migrations.AlterField(
            model_name='song',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 20, 4, 41, 48941)),
        ),
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='video',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 20, 4, 41, 144968)),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to='%d%m%y'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
