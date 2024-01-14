from django.db import models

class Workers(models.Model):
    full_name = models.CharField(max_length=30)
    # worker_id = models.IntegerField(primary_key=True)
    email = models.EmailField(default='empty@empty.com')
    address = models.CharField(default="Elad", max_length=30)

    def __str__(self):
        return str(self.full_name)
