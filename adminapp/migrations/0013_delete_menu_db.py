# Generated by Django 5.1 on 2024-09-22 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0012_product_db_remove_menu_db_image2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='menu_db',
        ),
    ]
