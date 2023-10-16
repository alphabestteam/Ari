from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from targets.models import Target
from targets.serializers import TargetSerializer
import json

@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = TargetSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.create(object_data).save()
            return HttpResponse("the target was saved!")
        else:
            return HttpResponse("the object is not well-formed")
   

@csrf_exempt
def update_target(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        target_id = data["target_id"]
        target = Target.objects.get(target_id=target_id)
        target_serialized = TargetSerializer(target, data=data)
        if target_serialized.is_valid():
            target_serialized.update(target, data).save()
            return JsonResponse({"the target updated!"}, safe=False, status=status.HTTP_200_OK)
        return HttpResponse("Something want wrong!", status=status.HTTP_400_BAD_REQUEST)
    
def all_targets(request):
    if request.method == 'GET':
        target = Target.objects.all()
        target_serialized = TargetSerializer(target,many=True)
        return JsonResponse(target_serialized.data,safe=False)