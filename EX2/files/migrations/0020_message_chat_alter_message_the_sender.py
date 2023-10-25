# Generated by Django 4.2.6 on 2023-10-25 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_unread_messages'),
        ('files', '0019_alter_message_the_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='File', to='files.eventchat'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='the_sender',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
