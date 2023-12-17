# # from django.shortcuts import get_object_or_404
# # from rest_framework.decorators import api_view
# # from taken.serializers import TakenSerializers
# # from items.serializers import ItemSerializers
# # from taken.models import Taken
# # from items.models import Items
# # from rest_framework.response import Response


# # @api_view(["POST", "GET"])
# # def take_item(request):
# #     taken_items = []
# #     if request.method == "POST":
# #         object_data = request.data
# #         item_pk = object_data["item_id"]
# #         data_deserialized = TakenSerializers(data=object_data)
# #         if data_deserialized.is_valid():
# #             taken =  data_deserialized.save()
# #             item = get_object_or_404(Items, item_id=item_pk)
# #             taken.taken_by.add(item)
# #             return Response("The item was taken successfully!")
# #         return Response(data_deserialized.errors)

# #     if request.method == "GET":
# #         taken = Taken.objects.all()
# #         taken_serialized = TakenSerializers(taken, many = True)
# #         return Response(taken_items)

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Taken, Items 
# from .serializers import ItemSerializers, TakenSerializers

# @api_view(['POST', 'GET'])
# def take_item(request, item_id):
#     if request.method == "POST":
#         user_id = request.data.get('user_id')  

#         try:
#             item = Items.objects.get(item_id=item_id)  
#         except Items.DoesNotExist:
#             return Response({"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

#         taken_item = Taken.objects.create(item=item, taken_by_id=user_id)
#         serializer = TakenSerializers(taken_item)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # if request.method == "GET":
#     #     try:
#     #         taken_items = Taken.objects.filter(taken_by_id=user_id)
#     #     except Taken.DoesNotExist:
#     #         return Response({"detail": "No taken items found for the user."}, status=status.HTTP_404_NOT_FOUND)

#     #     serializer = TakenSerializers(taken_items, many=True)
#     #     return Response(serializer.data, status=status.HTTP_200_OK)

