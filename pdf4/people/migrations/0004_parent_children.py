# Generated by Django 4.2.6 on 2023-10-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(related_name='Children', to='people.people'),
        ),
    ]
