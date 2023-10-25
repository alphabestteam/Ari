from django.urls import path
from . import views

urlpatterns = [
    path("AllEvents/", views.all_events),
    path("AddEvent/", views.add_event),
    path("UpdateEvent/", views.update_event),
    path("DeleteEvent/<int:id>/", views.delete_event),

    path("AllChats/", views.all_chats),
    path("AddChat/", views.add_chat),

    path("AllMessageFile/", views.all_message_file),
    path("AddMessageFile/", views.add_message_file),
    path("UpdateMessageFile/", views.update_message_file),
    path("DeleteMessageFile/<int:id>/", views.delete_message_file),
    # path("FindMessage/<int:id>", views.find_message_by_chat),

    path("AllSharedFile/", views.all_shared_file),
    path("AddSharedFile/", views.add_shared_file), 
    path("DeleteSharedFile/", views.delete_shared_file),  
    path("UpdateMessageFile/", views.update_message_file),
    
]