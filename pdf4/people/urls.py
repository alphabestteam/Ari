from django.urls import path
from . import views

urlpatterns = [
    path("AllPeople/", views.all_people, name = "allPeople"),
    path("AddPeople/", views.add_people, name = "addPeople"),
    path("UpdatePeople/", views.update_people, name = "updatePeople"),
    path("DeletePeople/<int:id>/", views.delete_people, name = "deletePeople"),
    path("AllParent/", views.all_parent, name = "allParent"),
    path("AddParent/", views.add_parent, name = "addParent"),
    path("UpdateParent/", views.update_parent, name = "updateParent"),
    path("DeleteParent/<int:id>/", views.delete_parent, name = "deleteParent"),
    path("RelatedParent/", views.related_parent, name = "relatedParent"),
    path("SpecificParent/<int:id>/", views.specific_parent, name = "specificParent"),
    path("RichParent/", views.rich_parent, name = "richParent"),
    path("FindParent/<int:id>/", views.find_parent, name = "findParent"),
    path("FindChild/<int:id>/", views.find_child, name = "findChild"),
    path("FindGrand/<int:id>/", views.find_grand, name = "findGrand"),
    path("FindSiblings/<int:id>/", views.find_siblings, name = "findSiblings"),
]