# Generated by Django 3.2 on 2021-08-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teracota', '0022_alter_myorder_kartimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='special1',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
