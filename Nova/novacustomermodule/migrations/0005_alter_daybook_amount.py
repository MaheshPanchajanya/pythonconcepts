# Generated by Django 3.2.3 on 2021-07-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novacustomermodule', '0004_alter_daybook_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='amount',
            field=models.CharField(max_length=15),
        ),
    ]
