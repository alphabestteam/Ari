from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import People
from people.serializers import PeopleSerializers
import json


@csrf_exempt
def add_people(request):
    if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = PeopleSerializers(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("The person saved!")
        return HttpResponse("Something want wrong")

@csrf_exempt
def update_people(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        people_id = data["people_id"]
        people = People.objects.get(people_id=people_id)
        people_serialized = PeopleSerializers(people, data=data)
        if people_serialized.is_valid():
            people_serialized.save()
            return HttpResponse("the person updated!")
        return HttpResponse("Something want wrong!")
    
@csrf_exempt
def delete_people(request, id):
    try:
        if request.method == 'DELETE':
            people = People.objects.get(people_id=id)
            people.delete()
            return HttpResponse({"The person was deleted!"})
    except:
        return HttpResponse("This person not exist!")



@csrf_exempt
def all_people(request):
    if request.method == 'GET':
        people = People.objects.all() 
        people_serialized = PeopleSerializers(people, many=True)
        return JsonResponse(people_serialized.data, safe=False)