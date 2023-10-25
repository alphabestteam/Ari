from django.db import models
from users.models import User


class File(models.Model):
    OPTIONS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Waiting for Response', 'Waiting for Response'),
        ('Waiting for Handling', 'Waiting for Handling'),
    )
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_open = models.DateField(auto_now=True) 
    event_status = models.CharField(max_length=20, choices=OPTIONS, default='Open')
    open_draft = models.BooleanField(default=False)
    sand_archive = models.BooleanField(default=False)
    event_id = models.IntegerField(primary_key=True)
    date_close = models.DateField(auto_now=True)
    shared_members= models.ManyToManyField(User, related_name='File', blank=True)

class EventChat(File):
    chat_id = models.IntegerField()

class Message(models.Model):
    text = models.TextField()
    send_date = models.DateField(auto_now=True)
    the_sender = models.OneToOneField(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(EventChat, on_delete=models.CASCADE, related_name='File', blank=True)

class EventShare(File):
    upload_date = models.DateField(auto_now=True)
    the_uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    # the_file = models.FileField(upload_to='/')


