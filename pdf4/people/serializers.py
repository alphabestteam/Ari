from rest_framework import serializers
from .models import People, Parent

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = "__all__"

        def update(self, instance, validated_data):
            instance.name = validated_data.get("name", instance.name)
            instance.date_of_birth = validated_data.get("date_of_birth", instance.date_of_birth)
            instance.city = validated_data.get("city", instance.city)
            instance.save()
            return instance

class ParentSerializers(PeopleSerializers):
    class Meta:
        model = Parent
        fields = "__all__"   

    def update(self, instance, validated_data):
        instance.work_place = validated_data.get("work_place", instance.work_place)
        instance.salary = validated_data.get("salary", instance.salary)
        super(PeopleSerializers, self).update(instance, validated_data)
        return instance