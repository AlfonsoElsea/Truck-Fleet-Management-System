# Generated by Django 4.0.5 on 2022-07-08 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truckregister', '0006_alter_driver_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='truck',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='truckregister.truck'),
        ),
    ]