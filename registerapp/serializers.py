
from rest_framework import serializers
from .models import registermodel
class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = registermodel
        fields = ['name', 'password', 'email']
    def create(self, validated_data):
        return registermodel.objects.create(**validated_data)