from rest_framework import serializers
from users.models import User

class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    class Meta: 
        model = User
        fields = ['id', 'email', 'full_name', 'password', 'is_admin']

