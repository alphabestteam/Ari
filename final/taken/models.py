# from django.db import models
# from users.models import User
# from items.models import Items
# from django.contrib.postgres.fields import ArrayField


# class Taken(models.Model):
#     taken_by = models.ForeignKey(User, related_name="taken_items", on_delete=models.CASCADE, default=None, null=True)
#     item = models.ForeignKey(Items, related_name="taken_items", on_delete=models.CASCADE)
#     taken_items = models.CharField(max_length=50, blank=True, null=True)
#     taken_date = models.TimeField(auto_now=True)   
#     return_date = models.TimeField(auto_now=True) 

#     def __str__(self):
#         return str(self.taken_items) 


