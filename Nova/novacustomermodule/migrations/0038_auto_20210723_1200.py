# Generated by Django 3.2.3 on 2021-07-23 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novacustomermodule', '0037_auto_20210723_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techsupport',
            name='endtime',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='techsupport',
            name='st',
            field=models.TimeField(default=datetime.datetime(2021, 7, 23, 12, 2, 41, 391998)),
        ),
        migrations.AlterField(
            model_name='techsupport',
            name='starttime',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='techsupport',
            name='totaltime',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
