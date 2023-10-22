from django.db import models
from datetime import date

class People(models.Model):
    name = models.CharField(max_length = 20)
    people_id = models.IntegerField(primary_key=True)
    date_of_birth = models.DateTimeField()
    city = models.CharField(max_length = 20)

    def adult_person(self):
        current_date = date.today()
        age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age >= 18
    
class Parent(People):
    work_place = models.CharField(max_length = 30)
    salary = models.IntegerField(max_length= 8)
    children = models.ManyToManyField(People, related_name = "parents", default = [])


    def __str__(self):
        return f"Name: {self.name}, Id: {self.people_id}, Birth: {self.date_of_birth}, City: {self.city}, Work place: {self.work_place}, salary: {self.salary}, Children: {self.children}"
    


