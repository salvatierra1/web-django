# Generated by Django 5.0.7 on 2024-07-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=500)),
                ('mail', models.EmailField(max_length=100)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
    ]
