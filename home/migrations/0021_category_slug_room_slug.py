# Generated by Django 4.0.6 on 2022-08-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_booking_check_in_alter_booking_check_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='a'),
        ),
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(default='a'),
        ),
    ]
