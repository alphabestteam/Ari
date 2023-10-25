from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from users.serializers import UserSerializers
# from files.serializers import MessageSerializers 
from users.models import User
# from files.models import Event


@api_view(["POST"])  
def add_user(request):
    object_data = request.data
    data_deserialized = UserSerializers(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The user saved!")
    return Response("Something want wrong")


@api_view(["PUT"]) 
def update_user(request):
    data = request.data 
    user_id = data["user_id"]
    user = get_object_or_404(User, user_id=user_id)
    user_serialized = UserSerializers(user, data=data)
    if user_serialized.is_valid():
        user_serialized.save()
        return Response("the user updated!")
    return Response("Something in update user want wrong!")


@api_view(["DELETE"])
def delete_user(request, id):
    user = get_object_or_404(User, user_id=id)
    user.delete()
    return Response("The user was deleted!")


@api_view(["GET"])
def all_users(request):
    user = User.objects.all()
    user_serialized = UserSerializers(user, many=True)
    return Response(user_serialized.data)

# @api_view(["GET"])
# def find_users_and_message(request, id):
#     user = User.objects.get(user_id=id)
#     user_serializer = UserSerializers(user)
#     message = File.message.all()
#     message_serializer = MessageSerializers(message, many=True)
#     response_data = {
#                 "user": user_serializer.data,
#                 "message": message_serializer.data,
#             }
#     return Response(response_data)