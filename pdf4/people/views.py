from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import People, Parent
from people.serializers import PeopleSerializers, ParentSerializers
from django.db.models import Q
import json
import datetime 



@csrf_exempt
def add_people(request):
        if request.method == 'POST':
            try:
                object_data = JSONParser().parse(request)
                data_deserialized = PeopleSerializers(data=object_data)
                if data_deserialized.is_valid():
                    data_deserialized.save()
                    return HttpResponse("The person saved!", status=200)
            except:
                return HttpResponse("Something want wrong", status=400)

@csrf_exempt
def update_people(request):
        if request.method == 'PUT':
            try:
                data = json.loads(request.body)
                people_id = data["people_id"]
                people = People.objects.get(people_id=people_id)
                people_serialized = PeopleSerializers(people, data=data)
                if people_serialized.is_valid():
                    people_serialized.save()
                    return HttpResponse("the person updated!", status=200)
            except:
                return HttpResponse("Something in add people want wrong!", status=400)
    
@csrf_exempt
def delete_people(request, id):
    
        if request.method == 'DELETE':
            try:
                people = People.objects.get(people_id=id)
                people.delete()
                return HttpResponse({"The person was deleted!"}, status=200)
            except:
                return HttpResponse("This person not exist!", status=400)



@csrf_exempt
def all_people(request):
    if request.method == 'GET':
        people = People.objects.all() 
        people_serialized = PeopleSerializers(people, many=True)
        return JsonResponse({"All people":people_serialized.data}, safe=False, status=200)
    

                               # ------------------------------------------------------------- parent -------------------------------------------------- #                                                                                     
@csrf_exempt
def add_parent(request):
    if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = ParentSerializers(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return HttpResponse("The parent saved!", status=200)
        return HttpResponse("Something in add parent want wrong", status=400)


@csrf_exempt
def update_parent(request):
        if request.method == 'PUT':
            try:    
                data = json.loads(request.body)
                people_id = data["people_id"]
                parent = Parent.objects.get(people_id=people_id)
                parent_serialized = ParentSerializers(parent, data=data)
                if parent_serialized.is_valid():
                    parent_serialized.save()
                    return HttpResponse("the parent updated!", status=200)
            except:
                return HttpResponse("Could'nt update this id!", status=400)
    
@csrf_exempt
def delete_parent(request, id):
        if request.method == 'DELETE':
            try:
                people = People.objects.get(people_id=id)
                people.delete()
                return HttpResponse("The parent was deleted!", status=200)
            except:
                return HttpResponse("This parent not exist!", status=400)


@csrf_exempt
def all_parent(request):
    if request.method == 'GET':
        parent = Parent.objects.all() 
        parent_serialized = ParentSerializers(parent, many=True)
        return JsonResponse({"all parents":parent_serialized.data}, safe=False, status=200)
    
@csrf_exempt
def related_parent(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            parent_id = data.get("parent_id")
            child_id = data.get("children_id")
            parent = Parent.objects.get(people_id=parent_id)
            child = People.objects.get(people_id=child_id)
            parent.children.add(child)
            return HttpResponse("Child related to his parent. Congratulations!", status=200)
        except:
            return HttpResponse("The parent's or child's id has a problem, please check again and retry.", status=400)


@csrf_exempt
def specific_parent(request, id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(people_id=id)
            parent_serializer = ParentSerializers(parent)  
            children = parent.children.all()
            children_serializer = PeopleSerializers(children, many=True)
            response_data = {
                "parent": parent_serializer.data,
                "children": children_serializer.data,
            }
            return JsonResponse(response_data, safe=False)
        except:
            return HttpResponse("Parent not found.",status=400)
    
@csrf_exempt
def rich_parent(request):
        if request.method == "GET":
            try:
                adult = datetime.datetime.now().year - 18
                rich = People.objects.filter(Q(parents__salary__gte=50000) & Q(date_of_birth__year__gte=adult))
                rich_data = [PeopleSerializers(rich_child).data for rich_child in rich]
                return JsonResponse({"Rich Children": rich_data}, safe=False, status=200)
            except:
                return HttpResponse("Not found parent in those condition!",status=400)
    
@csrf_exempt
def find_parent(request, id):
         if request.method == 'GET':
            try:
                child = Parent.objects.get(people_id = id)
                parents = ParentSerializers(child.parents.all(), many=True).data
                return JsonResponse({"Parents":parents}, safe=False, status=200)
            except: 
                return HttpResponse("Sorry, We can't found this children's parents. try again later", status=400) 

@csrf_exempt
def find_child(request, id):
         if request.method == 'GET':
            try:
                parent = Parent.objects.get(people_id = id)
                child = PeopleSerializers(parent.children.all(), many=True).data
                return JsonResponse({"Children":child}, safe=False, status=200)
            except: 
                return HttpResponse("Something want wrong to found this parent's children;( ", status=400)

@csrf_exempt
def find_grand(request, id):
         if request.method == 'GET':
            try:
                child = Parent.objects.get(people_id = id)
                parents = child.parents.all()
                grands = []
                for parent in parents:
                    grands.extend(parent.parents.all())
                grand_serializer = ParentSerializers(grands, many=True).data
                return JsonResponse({"Grands":grand_serializer}, safe=False, status=200)
            except:
                return HttpResponse ("can't find any grands", status=400)

@csrf_exempt
def find_siblings(request, id):
        if request.method == 'GET':
            try:
                child = Parent.objects.get(people_id = id)
                parents = child.parents.all()
                siblings = []
                for children in parents:
                    siblings.extend(children.children.all())
                sibling_serialized = PeopleSerializers(siblings, many=True).data
                return JsonResponse({"Siblings":sibling_serialized}, safe=False, status = 200)
            except:
                return HttpResponse("Can not found siblings to this child", status = 400)