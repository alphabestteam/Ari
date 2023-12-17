from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from users.serializers import UserSerializers
from users.models import User
from rest_framework.response import Response


@api_view(["POST", "GET"])
def create_and_get_users(request):
    if request.method == "POST":
        object_data = request.data
        data_deserialized = UserSerializers(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return Response("The user was created successfully!")
        return Response(data_deserialized.errors)

    # only users with admin permission can get the users
    if request.method == "GET":
        executerID = request.data["ex_id"]
        executer = get_object_or_404(User, user_id=executerID)
        if executer.is_admin != True:
            return Response("Access denied! You don't have permission")
        user = User.objects.all()
        user_serialized = UserSerializers(user, many=True)
        return Response(user_serialized.data)


# only users with admin permission can get a specific user
@api_view(["GET", "DELETE"])
def get_and_delete_specific_user(request, id):
    if request.method == "GET":
        executerID = request.data["ex_id"]
        executer = get_object_or_404(User, user_id=executerID)
        if executer.is_admin != True:
            return Response("Access denied! You don't have permission")
        user = get_object_or_404(User, user_id=id)
        user_serialized = UserSerializers(user)
        return Response(user_serialized.data)

    # only users with admin permission can delete a user
    if request.method == "DELETE":
        executerID = request.data["ex_id"]
        executer = get_object_or_404(User, user_id=executerID)
        if executer.is_admin != True:
            return Response("Access denied! You don't have permission")
        user = get_object_or_404(User, user_id=id)
        user.delete()
        return Response(f"The user was deleted by the admin {executer}!")