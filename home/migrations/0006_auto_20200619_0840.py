# Generated by Django 3.0.5 on 2020-06-19 03:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200619_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='busyTill',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
