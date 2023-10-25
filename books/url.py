from django.urls import path
from . import views

urlpatterns = [
    path("AllBooks/", views.all_books),
    path("AddBook/", views.add_book),
    path("UpdateBook/", views.update_book),
    path("DeleteBook/<int:id>/", views.delete_book),
    path("SearchBook/", views.search_book),
    path("UpdateField/<int:id>/", views.update_field),
]
