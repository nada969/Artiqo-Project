# Generated by Django 5.1.7 on 2025-04-09 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_user_id_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='user_id',
        ),
    ]
