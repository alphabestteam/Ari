# Generated by Django 4.2.6 on 2023-10-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0025_alter_message_the_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventchat',
            name='chat_id',
            field=models.IntegerField(auto_created=True),
        ),
    ]
