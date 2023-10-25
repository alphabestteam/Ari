from django.urls import path
from . import views

urlpatterns = [
    path("AllUsers/", views.all_users),
    path("AddUser/", views.add_user),
    path("UpdateUser/", views.update_user),
    path("DeleteUser/<int:id>/", views.delete_user),
    # path("FindAll/<int:id>/", views.find_users_and_message),
]