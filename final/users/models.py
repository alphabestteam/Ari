from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    user_id = models.IntegerField(primary_key=True, default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_clean)