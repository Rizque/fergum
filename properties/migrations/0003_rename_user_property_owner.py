# Generated by Django 4.1.7 on 2023-04-01 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_rename_owner_property_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='user',
            new_name='owner',
        ),
    ]