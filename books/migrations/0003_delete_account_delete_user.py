# Generated by Django 4.2.6 on 2023-10-23 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_user_alter_book_title_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
