from rest_framework import serializers
from items.models import Items

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ["taken", "item_name", "item_category", "city", "description", "phon_number", "id", "uploaded_by", "uploaded_date"]
