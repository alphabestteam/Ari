from django.db import models

class People(models.Model):
    name = models.CharField(max_length = 20)
    people_id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateTimeField()
    city = models.CharField(max_length = 20)
    
class Parent(People):
    work_place = models.CharField(max_length = 30)
    salary = models.DecimalField(max_digits = 8, decimal_places = 2)
    children = models.ManyToManyField(People, related_name = "parents", default = [])

    def __str__(self):
        return f"Name: {self.name}, Id: {self.people_id}, Birth: {self.date_of_birth}, City: {self.city}, Work place: {self.work_place}, salary: {self.salary}, Children: {self.children}"
    