# Generated by Django 3.2 on 2021-08-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teracota', '0021_alter_myorder_kartimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='kartimg',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
