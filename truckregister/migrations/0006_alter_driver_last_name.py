# Generated by Django 4.0.5 on 2022-06-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truckregister', '0005_alter_driver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
