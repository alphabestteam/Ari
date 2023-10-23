from rest_framework import serializers
from .models import Book, Author, Message, User

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["book_id"]  # Answer to question 14

    title_length = serializers.SerializerMethodField # Answer to question 13 and example for Question 15.
    def get_title_length(self, instance):
        return len(instance.title)

class AuthorSerializers(serializers.ModelSerializer): # I added this class so i can use the slug serializer for question 16.
    
    books = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Author
        fields = '_all_'

# The two following classes is answer for question 18 
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'  

class UserSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)  
    class Meta:
        model = User
        fields = '__all__'  
        depth = 1  

from decimal import Decimal






