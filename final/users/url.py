from django.urls import path
from . import views


urlpatterns = [
    path("users", views.create_and_get_users),
    path("users/<id>", views.get_and_delete_specific_user),
  
]