# Generated by Django 5.2 on 2025-04-26 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_advertisement_area_alter_advertisement_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adimage',
            name='image_name',
        ),
    ]
