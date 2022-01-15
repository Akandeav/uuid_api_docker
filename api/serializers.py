from rest_framework import serializers
from .models import UUIDValue

class UUIDSerializer(serializers.ModelSerializer):
    """
    Creates and saves instances in UUIDValue model
    Returns instance
    """
    class Meta:
        model = UUIDValue
        fields = ['time_stamp', 'uuid']
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance