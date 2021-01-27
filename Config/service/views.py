from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import UidStore, FarmStore, Result, CassavaArea, CassavaCheck
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import permissions 
from rest_framework import status 
from django.db.models import Count
from django.db.models.functions import math

# Create your views here.

@api_view(['GET', 'POST'])
def uid_collected(request) :
    if request.method == 'GET' :
        uids = UidStore.objects.all()
        serializer = UidStoreSerializer(uids, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UidStoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def uid_editor(request, pk) :
    try:
        uid = UidStore.objects.get(pk=pk)
    except UidStore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = UidStoreSerializer(uid)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializer = UidStoreSerializer(uid, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'uidupdate' : uid}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        uid.delete()
        return Response(print(pk + ' is deleted') ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def farm_list(request):
    if request.method == 'GET' :
        farmList = FarmStore.objects.all()
        serializer = FarmSerializer(farmList, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FarmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def farm_detail(request, pk):
    try:
        farmList = FarmStore.objects.get(pk=pk)
    except FarmStore.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = FarmSerializer(farmList)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializer = FarmSerializer(farmList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        farmList.delete()
        return Response(print(pk + ' is deleted') ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def result(request):
    result_data = Result.objects.all()
    serializer = ResultSerializers(result_data, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def cassava_check(request):
    if request.method == 'GET' :
        checked_data = CassavaCheck.objects.all()
        serializer = CassavaCheckSerializers(checked_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CassavaCheckSerializers(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def cassava_check_editor(request, pk) :
    try:
        checked_data = CassavaCheck.objects.get(pk=pk)
    except CassavaCheck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = CassavaCheckSerializers(checked_data)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializer = CassavaCheckSerializers(checked_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'checkdupdate' : checked_data}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        checked_data.delete()
        return Response(print(pk + ' is deleted') ,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def area_check_get(request):
    if request.method == 'GET' :
        areas_data = CassavaArea.objects.all()
        serializer = CassavaAreaSerializer(areas_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CassavaAreaSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

api_view(['PUT', 'DELETE'])
def area_check(request, pk) :
    try:
        areas = CassavaArea.objects.get(pk=pk)
    except CassavaArea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = CassavaAreaSerializer(areas)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializer = CassavaAreaSerializer(areas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'checkdupdate' : areas}, serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        areas.delete()
        return Response(print(pk + ' is deleted') ,status=status.HTTP_400_BAD_REQUEST)

def measure(lat1, lon1, lat2, lon2) :
    R = 6378.137; #Radius of earth in KM
    dLat = lat2 * math.Pi / 180 - lat1 * math.Pi / 180;
    dLon = lon2 * math.Pi / 180 - lon1 * math.Pi / 180;
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1 * math.Pi / 180) * math.cos(lat2 * math.Pi / 180) * math.sin(dLon/2) * math.sin(dLon/2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
    d = R * c;
    metar = d * 1000
    return metar, print("distance : " ,metar); #meters

api_view(['PUT', 'DELETE'])
def cassava_check_new(request, pk) :
    try:
        checked_data = CassavaCheck.objects.get(pk=pk)
    except CassavaCheck.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = CassavaCheckSerializers(checked_data)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializer = CassavaCheckSerializers(checked_data, data=request.data)
        if pk is None :
            serializer = CassavaCheckSerializers(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST), print("this is none of pk")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'checkdupdate' : checked_data}, serializer.errors, status=status.HTTP_400_BAD_REQUEST), print("this have pk")

    elif request.method == 'DELETE':
        checked_data.delete()
        return Response(print(pk + ' is deleted') ,status=status.HTTP_400_BAD_REQUEST)