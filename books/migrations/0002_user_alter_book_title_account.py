# Generated by Django 4.2.4 on 2023-10-23 11:24

import books.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, validators=[books.models.validate_title])),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=20, validators=[books.models.validate_title]),
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=20, validators=[books.models.validate_title])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.user')),
            ],
        ),
    ]
