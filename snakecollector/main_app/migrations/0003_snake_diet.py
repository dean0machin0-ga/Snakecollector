# Generated by Django 5.0.1 on 2024-01-12 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_snake_native_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='snake',
            name='diet',
            field=models.TextField(default='Food', max_length=125),
        ),
    ]
