# Generated by Django 5.1 on 2024-09-26 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pregnancyapp', '0002_alter_patient_db_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_db',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
