from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import students

class Studentserializers(serializers.ModelSerializer):
    
    # name = serializers.CharField(write_only = True)
    
    class Meta:
        model = students
        fields = [ 'roll', 'city']
    # model serializers give both the get and update method
    
    # validation 
    #field based validation
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat full')
        return value
    
    # object level validation
    # def validate(self, data):
    #     name = data.get('name')
    #     city = data.get('city')
    #     if name.lower() == city.lower() :
    #         raise serializers.ValidationError("Name of the city and person name cannot be same")
    #     return data