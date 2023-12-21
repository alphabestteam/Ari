from django.db import models
from  users.models import User

class Items(models.Model):
    uploaded_by = models.ForeignKey(User, related_name="item", on_delete=models.CASCADE, default=None, null=True)
    taken = models.BooleanField(default=False)
    uploaded_date = models.TimeField(auto_now=True)
    item_name = models.CharField(max_length=15)
    item_category = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    description = models.CharField(max_length=70)
    phon_number = models.IntegerField(max_length=9)
    image = models.ImageField(null=True, blank=True, upload_to="images/ ")
    
    def __str__(self):
        return str(self.uploaded_by)
