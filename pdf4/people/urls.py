from django.urls import path
from . import views

urlpatterns = [
    path("AllPeople/", views.all_people, name = "allPeople"),
    path("AddPeople/", views.add_people, name = "addPeople"),
    path("UpdatePeople/", views.update_people, name = "updatePeople"),
    path("DeletePeople/<int:id>/", views.delete_people, name = "deletePeople")
]