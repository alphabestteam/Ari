from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    user_id = models.IntegerField(primary_key=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user_id)