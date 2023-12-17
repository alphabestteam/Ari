from django.urls import path
from . import views

urlpatterns = [
    path("items", views.add_and_get_item),
    path("items/<id>", views.delete_and_get_item),
]