# Generated by Django 3.2 on 2021-05-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teracota', '0005_rename_feedpic_feed_picforblg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='properitorpic',
        ),
        migrations.AddField(
            model_name='about',
            name='cnc',
            field=models.ImageField(blank=True, null=True, upload_to='bof'),
        ),
    ]
