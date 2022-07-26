# Generated by Django 4.0.5 on 2022-07-29 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truckregister', '0007_alter_driver_truck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='truckregister.truck'),
        ),
    ]
