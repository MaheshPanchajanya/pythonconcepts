# Generated by Django 3.2.3 on 2021-07-31 05:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novacustomermodule', '0048_alter_techsupport_st'),
    ]

    operations = [
        migrations.AddField(
            model_name='techsupport',
            name='prfctdate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='techsupport',
            name='st',
            field=models.TimeField(default=datetime.datetime(2021, 7, 31, 11, 20, 6, 399273)),
        ),
    ]
