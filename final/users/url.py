from django.urls import path
from . import views


urlpatterns = [
    path("register", views.create_and_get_users),
    path("login", views.login),
    path("users/<id>", views.get_and_delete_specific_user),
  
]