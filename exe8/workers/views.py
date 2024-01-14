from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from workers.serializers import WorkerSerializers
from workers.models import Workers
from rest_framework.response import Response


# Post and Get endpoints
@api_view(["POST", "GET"])
def add_and_get_worker(request):
    if request.method == "POST":
        object_data = request.data
        data_deserialized = WorkerSerializers(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return Response("The worker was added successfully!")
        return Response(data_deserialized.errors)

    if request.method == "GET":
        worker = Workers.objects.all()
        worker_serialized = WorkerSerializers(worker, many=True)
        return Response(worker_serialized.data)


# Get, Delete, and Put a specifics workers endpoints
@api_view(["DELETE", "GET", "PUT"])
def get_edit_delete_worker(request, id):
    if request.method == "DELETE":
        worker = get_object_or_404(Workers, id=id)
        worker.delete()
        return Response("The worker was deleted successfully!")

    if request.method == "GET":
        worker = get_object_or_404(Workers, id=id)
        serializer = WorkerSerializers(worker)
        return Response(serializer.data)

    if request.method == "PUT":
        worker = get_object_or_404(Workers, id=id)
        serializer = WorkerSerializers(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
