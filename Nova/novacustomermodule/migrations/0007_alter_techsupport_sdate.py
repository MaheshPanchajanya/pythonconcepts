# Generated by Django 3.2.3 on 2021-07-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novacustomermodule', '0006_techsupport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techsupport',
            name='sdate',
            field=models.DateTimeField(),
        ),
    ]
