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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        return Response(print(pk + ' is deleted') ,status=status.HTTP_410_GONE)

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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['PUT', 'DELETE'])
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        areas.delete()
        return Response(print(pk + ' is deleted') ,status=status.HTTP_400_BAD_REQUEST)

#เครื่องทุกเครื่องต้องมี uid ของ user นั้นๆ
#เครื่องส่งค่า to cassava_check
#cassava_check ทำหน้าที่รับข้อมูลมาแล้วเทียบกับตำแหน่งของฟาร์มถ้าไม่เกินรัศมีให้อยู่ในฟาร์มนั้น(เทียบทุกข้อมูล)
#เขียนไงล่ะทีนี้
@api_view(['GET', 'POST'])
def cassava_check_farm(request, uid_store):
    checked_data = FarmStore.objects.filter(uid_store=uid_store)
    farm_lat_max = checked_data.values("latitude")
    farm_long_max = checked_data.values("longtitude")
    farm_lat_min = checked_data.values("latitude_mark2")
    farm_long_min = checked_data.values("longtitude_mark2")

    for i in range(len(farm_lat_max)):
        print(checked_data)
        print("farm lat1 " + str(farm_lat_max[i]['latitude']) 
        + " long1 " + str(farm_long_max[i]['longtitude']) + " lat2 " 
        + str(farm_lat_min[i]['latitude_mark2']) 
        + " long2 " + str(farm_long_min[i]['longtitude_mark2']))

    if request.method == 'GET' :
        serializer = FarmSerializer(checked_data, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def area_check_create(request, uid_store):
    checked_data = FarmStore.objects.filter(uid_store=uid_store)

    if request.method == 'GET' :
        areas_data = CassavaArea.objects.all()
        serializer = CassavaAreaSerializer(areas_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CassavaAreaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        for farm in checked_data :
            farm_lat_max = farm.latitude
            farm_lat_min = farm.latitude_mark2
            area_lat = serializer.validated_data['tree_latitude']
            farm_long_max = farm.longtitude_mark2
            farm_long_min = farm.longtitude
            area_long = serializer.validated_data['tree_longtitude']
            check_lat_range = float(farm_lat_max) >= float(area_lat) >= float(farm_lat_min)
            check_long_range = float(farm_long_max) >= float(area_long) >= float(farm_long_min)
            print("Lat = " + str(check_lat_range))
            print("Long = " + str(check_long_range))
            if (check_lat_range & check_long_range):
                print("We in " + str(farm.farm_id) + " " + str(serializer.validated_data))
                serializer.validated_data['farm_store'] = farm
                print(serializer.validated_data)
                serializer.save()
        return Response(serializer.data['cassava_area_id'], status=status.HTTP_201_CREATED)
