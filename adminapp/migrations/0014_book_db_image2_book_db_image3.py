# Generated by Django 5.1 on 2024-09-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_delete_menu_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_db',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AddField(
            model_name='book_db',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
    ]