# Generated by Django 5.1.6 on 2025-03-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=500)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[(1, 'Admin'), (2, 'Artist'), (3, 'Client')], max_length=1)),
            ],
        ),
    ]
