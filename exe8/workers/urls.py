from django.urls import path
from . import views

urlpatterns = [
    path("workers", views.add_and_get_worker),
    path("workers/<id>", views.get_edit_delete_worker),
]