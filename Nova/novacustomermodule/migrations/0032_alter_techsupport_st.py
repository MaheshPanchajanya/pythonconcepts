# Generated by Django 3.2.3 on 2021-07-22 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novacustomermodule', '0031_alter_techsupport_st'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techsupport',
            name='st',
            field=models.TimeField(default=datetime.datetime(2021, 7, 22, 14, 32, 9, 68277)),
        ),
    ]
