from django.db import models
from django.core.exceptions import ValidationError


def validate_title(value):  # Answer for Question 10
    if len(value) >= 100:
        raise ValidationError("The title is too long, The max size is 100 letters!")


class Book(models.Model):
    title = models.CharField(max_length=20, validators=[validate_title])
    author = models.CharField(max_length=50)
    published_date = models.DateTimeField()
    book_id = models.IntegerField(primary_key=True)


class Author(models.Model):
    author_id = models.IntegerField(max_length=10)
    author_name = models.CharField(max_length=20)


# The two following classes is answer for question 18:
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.user.name} - {self.timestamp}"
