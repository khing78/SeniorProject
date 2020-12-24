from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def List(request):
    showEmails = UidStore.objects.all()
    serializer = UidStoreSerializer(showEmails, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Detail(request, id):
    showEmails = UidStore.objects.get(id=id)
    serializer = UidStoreSerializer(showEmails, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Update(request, id):
    email = UidStore.objects.get(id=id)
    serializer = UidStoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def Delete(request, id):
    email = UidStore.objects.get(id=id)
    email.id.delete

    return Response("It Goneeeee")

class FarmsViewSet (ModelViewSet):
    queryset = FarmStore.objects.all()
    serializers_class = FarmSerializer