# Generated by Django 4.2.4 on 2023-12-17 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taken', '0004_taken_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Taken',
        ),
    ]