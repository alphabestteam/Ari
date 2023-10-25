from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from books.serializers import BookSerializers, AuthorSerializers
from books.models import Book, Author


@api_view(["POST"])  # I used with what requested in Question 2
def add_book(request):
    object_data = request.data  # I used with what requested in Question 2
    data_deserialized = BookSerializers(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The book saved!")
    return Response("Something want wrong")


@api_view(["PUT"])  # I used with what requested in Question 2
def update_book(request):
    data = request.data  # I used with what requested in Question 2
    book_id = data["book_id"]
    book = get_object_or_404(Book, book_id=book_id)
    book_serialized = BookSerializers(book, data=data)
    if book_serialized.is_valid():
        book_serialized.save()
        return Response("the book updated!")
    return Response("Something in update book want wrong!")


@api_view(["DELETE"])
def delete_book(request, id):
    book = get_object_or_404(Book, book_id=id)
    book.delete()
    return Response("The parent was deleted!")


@api_view(["GET"])
def all_books(request):
    book = Book.objects.all()
    book_serialized = BookSerializers(book, many=True)
    return Response(book_serialized.data)


@api_view(["GET"])
def search_book(request):
    author = request.query_params["author"]  # I used with what requested in Question 3
    book = Book.objects.filter(author=author)
    book_serializer = BookSerializers(book, many=True)
    return Response(book_serializer.data)


@api_view(["POST"])  # Answer to question 11
def update_field(request, id):
    data = request.data
    book = get_object_or_404(Book, book_id=id)
    book_serialized = BookSerializers(book, data=data, partial=True)
    if book_serialized.is_valid():
        book_serialized.save()
        return Response("the field updated!")
    return Response("Something in update this field want wrong!")


# The two following function is for using slug in question 16
@api_view(["POST"])
def add_author(request):
    serializer = AuthorSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def find_books_by_author(request, author_id):
    author = get_object_or_404(Author, author_id=author_id)
    books = Book.objects.filter(author=author)
    serializer = BookSerializers(books, many=True)
    return Response(serializer.data)
