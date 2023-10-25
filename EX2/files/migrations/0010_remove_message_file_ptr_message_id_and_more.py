# Generated by Django 4.2.6 on 2023-10-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0009_eventchat_eventshare_delete_share_alter_message_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='file_ptr',
        ),
        migrations.AddField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.IntegerField(blank=True),
        ),
        migrations.DeleteModel(
            name='EventChat',
        ),
    ]
