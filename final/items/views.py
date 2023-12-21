from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from items.serializers import ItemSerializers
from items.models import Items
from rest_framework.response import Response 

@api_view(["POST", "GET"]) 
def add_and_get_item(request):

    if request.method == "POST":
        object_data = request.data
        data_deserialized = ItemSerializers(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.save()
            return Response("The item was added successfully!")
        return Response(data_deserialized.errors)
        
        
    if request.method == "GET":
        item = Items.objects.all()
        item_serialized = ItemSerializers(item, many=True)
        return Response(item_serialized.data)
    
# only the uploader can delete the item   
@api_view(["DELETE", "GET", "PUT"])
def delete_and_get_item(request, id):
    if request.method == "DELETE":
        # executerID = int(request.data.get("ex_id"))
        item = get_object_or_404(Items, id=id)
        # if executerID != item.uploaded_by.id:
        #     return Response("Access denied! don't have permission")
        # print(type(item.uploaded_by.is_admin))
        # if item.uploaded_by.is_admin == True:
        #     return Response("The item was deleted by the admin!")
        item.delete()
        return Response("The item was deleted by the uploader!")
    
# The uploader cen get all his items    
    if request.method == "GET":
        user_items = Items.objects.filter(uploaded_by=id)
        serializer = ItemSerializers(user_items, many=True)
        return Response(serializer.data)

# The uploader cen update his items    
    if request.method == 'PUT':
        item = Items.objects.get(pk=id)
        serializer = ItemSerializers(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
     


