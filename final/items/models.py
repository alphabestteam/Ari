from django.db import models
from  users.models import User

class Items(models.Model):
    uploaded_by = models.ForeignKey(User, related_name="item", on_delete=models.CASCADE, default=None, null=True)
    taken_by = models.ForeignKey(User, related_name="taken", on_delete=models.CASCADE, default=None, null=True)
    uploaded_date = models.TimeField(auto_now=True)
    item_name = models.CharField(max_length=15)
    item_category = models.CharField(max_length=30)
    item_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=20)
    description = models.CharField(max_length=70)

    def __str__(self):
        return str(self.uploaded_by)
