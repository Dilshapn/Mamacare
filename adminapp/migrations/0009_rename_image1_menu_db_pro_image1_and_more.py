# Generated by Django 5.1 on 2024-09-21 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_remove_menu_db_benefit_remove_menu_db_ingredients_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu_db',
            old_name='image1',
            new_name='pro_image1',
        ),
        migrations.RenameField(
            model_name='menu_db',
            old_name='image2',
            new_name='pro_image2',
        ),
        migrations.RenameField(
            model_name='menu_db',
            old_name='image3',
            new_name='pro_image3',
        ),
    ]
