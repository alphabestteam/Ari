from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=20, unique=False)
    password = models.CharField(max_length=20)
    email = models.EmailField(unique=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return str(self.full_clean)