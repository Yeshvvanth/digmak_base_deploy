# Generated by Django 3.1 on 2020-08-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountant',
            name='hour_rate',
            field=models.FloatField(),
        ),
    ]