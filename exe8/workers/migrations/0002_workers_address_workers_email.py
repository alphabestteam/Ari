# Generated by Django 5.0 on 2024-01-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='address',
            field=models.CharField(default='Elad', max_length=30),
        ),
        migrations.AddField(
            model_name='workers',
            name='email',
            field=models.EmailField(default='empty@empty.com', max_length=254),
        ),
    ]
