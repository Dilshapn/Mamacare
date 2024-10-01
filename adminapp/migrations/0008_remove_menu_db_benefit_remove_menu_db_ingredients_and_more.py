# Generated by Django 5.1 on 2024-09-21 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_book_db_alter_menu_db_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_db',
            name='benefit',
        ),
        migrations.RemoveField(
            model_name='menu_db',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='menu_db',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
        migrations.AddField(
            model_name='menu_db',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]