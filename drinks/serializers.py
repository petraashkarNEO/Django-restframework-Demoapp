# this to convert from python object to JSON
from .models import Drink
from rest_framework import serializers

class DrinkSerializer(serializers.ModelSerializer):
    # inter class Meta (metadata describing the model)
    class Meta: 
        model = Drink
        fields = ['id', 'name', 'description']