from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/targets/", include("targets.urls")),
    path('admin/', admin.site.urls)
    
]
