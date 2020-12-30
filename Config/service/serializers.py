from rest_framework import serializers

from .models import *

class UidStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UidStore
        fields = ('__all__')

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmStore
        fields = ('__all__')