from django.urls import path
from . import views

urlpatterns = [
  path("AddTarget/", views.add_target, name ="addTarget"),
  path("AllTargets/", views.all_targets, name ="allTarget"),
  path("UpdateTarget/", views.update_target, name = "updateTarget")

]
