# Generated by Django 5.1 on 2024-09-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pregnancyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_db',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
