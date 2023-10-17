from django.db import models

class People(models.Model):
    name = models.CharField(max_length=20)
    people_id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateTimeField()
    city = models.CharField(max_length=20)

def __str__(self):
    return f"Name: {self.name}, Id: {self.id}, Birth: {self.data_of_birth}, City: {self.city}"