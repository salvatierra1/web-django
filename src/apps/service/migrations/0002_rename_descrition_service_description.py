# Generated by Django 5.0.7 on 2024-07-26 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='descrition',
            new_name='description',
        ),
    ]