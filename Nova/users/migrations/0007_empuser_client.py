# Generated by Django 3.2.3 on 2021-07-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_empuser_techsup'),
    ]

    operations = [
        migrations.AddField(
            model_name='empuser',
            name='client',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
