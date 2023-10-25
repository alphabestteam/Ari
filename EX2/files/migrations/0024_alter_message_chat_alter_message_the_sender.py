# Generated by Django 4.2.6 on 2023-10-25 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_unread_messages'),
        ('files', '0023_alter_message_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='File', to='files.eventchat'),
        ),
        migrations.AlterField(
            model_name='message',
            name='the_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
