# Generated by Django 3.2.3 on 2021-07-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_empuser_updateflag'),
    ]

    operations = [
        migrations.AddField(
            model_name='empuser',
            name='nameflag',
            field=models.BooleanField(default=False),
        ),
    ]
