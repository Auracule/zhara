# Generated by Django 4.0.6 on 2022-07-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_category_description_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
    ]
