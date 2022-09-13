from os import stat
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request):

    # get all the drinks
    # serialize them
    # return JSON
    if request.method == 'GET':          
        drinks = Drink.objects.all() 
        serializer = DrinkSerializer(drinks, many=True) # many = True to serialize all the objects, serialize querysets 
        return Response(serializer.data)  
        # return JsonResponse(serializer.data) --> just return json response (JSON specific)

    # deserialize 
    if request.method == 'POST':
        serializer = DrinkSerializer(data= request.data)
        
        if serializer.is_valid(): # Check if data is valid , Deserializes and validates incoming data.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk=id)

    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':    
        serializer = DrinkSerializer(drink)
        return Response(serializer.data) # returns json response or HTML
    
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data= request.data)
        if serializer.is_valid(): # Check if data is valid
            serializer.save()  #  Persists the validated data into an object instance.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Returns any errors during validation.

    elif  request.method == 'DELETE': 
        drink.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)