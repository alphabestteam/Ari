from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    user_id = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()
    unread_messages = models.BooleanField(default=True)
    
    def __str__(self):
        return self.username
