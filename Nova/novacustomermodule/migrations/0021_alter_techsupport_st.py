# Generated by Django 3.2.3 on 2021-07-15 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novacustomermodule', '0020_alter_techsupport_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techsupport',
            name='st',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 18, 31, 15, 806035)),
        ),
    ]
