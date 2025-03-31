# Generated by Django 5.1.7 on 2025-03-30 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_remove_order_order_id_order_item'),
        ('users', '0003_remove_users_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_email', models.EmailField(max_length=254)),
                ('art_name', models.CharField(max_length=255)),
                ('story', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
