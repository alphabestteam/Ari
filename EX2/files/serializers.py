from rest_framework import serializers
from .models import File, Message, EventShare, User, EventChat

class FileSerializers(serializers.ModelSerializer):
    shared_members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = File
        fields = "__all__"


class ChatSerializers(FileSerializers):
        class Meta:
            model = EventChat
            fields = "__all__"


            
class MessageSerializers(FileSerializers):
        class Meta:
            model = Message
            fields = "__all__"

class ShareSerializers(FileSerializers):
        class Meta:
            model = EventShare
            fields = "__all__"