from django.urls import path
from .  import  views

urlpatterns = [
    path ("", views.home, name="home"),
    path ("api/getrandomnumber/", views.random_number, name="random_number"),
    path("api/getrandomnumber/<number>", views.user_number, name="user_number"),
    path("api/getservertime/", views.current_time, name="current_time"),
    path("api/getLengthOfWord/<word>", views.len_word, name="word")
]
