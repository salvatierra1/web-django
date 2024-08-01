# Generated by Django 5.0.7 on 2024-07-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(choices=[('Facebook', 'fa-brands fa-facebook'), ('Instagram', 'fa-brands fa-instagram'), ('Whatsapp', 'fa-brands fa-whatsapp')], default='Facebook', max_length=50, verbose_name='Icon')),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
