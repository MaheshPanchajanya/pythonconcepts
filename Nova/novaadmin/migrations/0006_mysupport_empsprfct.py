# Generated by Django 3.2.3 on 2021-07-31 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novaadmin', '0005_auto_20210728_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysupport',
            name='empsprfct',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
