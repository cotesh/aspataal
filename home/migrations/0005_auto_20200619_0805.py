# Generated by Django 3.0.5 on 2020-06-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_doctor_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='appointTime',
            field=models.DateTimeField(blank=True),
        ),
    ]
