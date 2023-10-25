from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from files.serializers import FileSerializers, MessageSerializers, ShareSerializers, ChatSerializers
from files.models import File, Message, EventShare, EventChat


@api_view(["POST"])  
def add_event(request):
    object_data = request.data
    data_deserialized = FileSerializers(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The event saved!")
    return Response("Something want wrong")


@api_view(["PUT"]) 
def update_event(request):
    data = request.data 
    event_id = data["event_id"]
    event = get_object_or_404(File, event_id=event_id)
    event_serialized = FileSerializers(event, data=data)
    if event_serialized.is_valid():
        event_serialized.save()
        return Response("the event updated!")
    return Response("Something in update event want wrong!")


@api_view(["DELETE"])
def delete_event(request, id):
    event = get_object_or_404(File, event_id=id)
    event.delete()
    return Response("The event was deleted!")


@api_view(["GET"])
def all_events(request):
    event = File.objects.all()
    event_serialized = FileSerializers(event, many=True)
    return Response(event_serialized.data)


# ------------------------------------------               chat                ------------------------------------------

@api_view(["POST"])  
def add_chat(request):
    object_data = request.data
    data_deserialized = ChatSerializers(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The shared chat saved!")
    return Response("Something want wrong")

@api_view(["GET"])
def all_chats(request):
    chat = EventChat.objects.all()
    chat_serialized = ChatSerializers(chat, many=True)
    return Response(chat_serialized.data)




# -------------------------------------------           message file        -------------------------------------------

@api_view(["POST"])  
def add_message_file(request):
    object_data = request.data
    data_deserialized = MessageSerializers(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The message saved!")
    return Response("Something want wrong")


@api_view(["PUT"]) 
def update_message_file(request):
    data = request.data 
    message_id = data["event_id"]
    message = get_object_or_404(Message, event_id=message_id)
    message_serialized = MessageSerializers(message, data=data)
    if message_serialized.is_valid():
        message_serialized.save()
        return Response("the message file updated!")
    return Response("Something in update event want wrong!")


@api_view(["DELETE"])
def delete_message_file(request, id):
    message = get_object_or_404(File, event_id=id)
    message.delete()
    return Response("The message file was deleted!")


@api_view(["GET"])
def all_message_file(request):
    message = Message.objects.all()
    message_serialized = MessageSerializers(message, many=True)
    return Response(message_serialized.data)

# @api_view(['GET'])
# def find_message_by_chat(request, id):
#     message = ChatSerializer.objects.get(event_id = id)
#     chat = ChatSerializer(message.chat.all(), many=True)
#     return Response(chat)


# ---------------------------------------------------       shared files      --------------------------------------------------

@api_view(["POST"])  
def add_shared_file(request):
    object_data = request.data
    data_deserialized = ShareSerializers(data=object_data)
    if data_deserialized.is_valid():
        data_deserialized.save()
        return Response("The shared message saved!")
    return Response("Something want wrong")

@api_view(["DELETE"])
def delete_shared_file(request, id):
    share = get_object_or_404(EventShare, event_id=id)
    share.delete()
    return Response("The shared message file was deleted!")

@api_view(["PUT"]) 
def update_shared_file(request):
    data = request.data 
    message_id = data["event_id"]
    message = get_object_or_404(Message, event_id=message_id)
    message_serialized = MessageSerializers(message, data=data)
    if message_serialized.is_valid():
        message_serialized.save()
        return Response("the shared message file updated!")
    return Response("Something in update shared message want wrong!")

@api_view(["GET"])
def all_shared_file(request):
    share = EventShare.objects.all()
    share_serialized = ShareSerializers(share, many=True)
    return Response(share_serialized.data)




