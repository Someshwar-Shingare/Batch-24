from rest_framework import serializers
from testapp1.models import Employee

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    sal = serializers.FloatField()
    address = serializers.CharField(max_length=100)


    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.eno = validated_data.get("eno", instance.eno)
        instance.name = validated_data.get("name", instance.name)
        instance.sal = validated_data.get("sal", instance.sal)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance
    