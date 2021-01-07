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

class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('_all_')

class CassavaCheckSerializers(serializers.ModelSerializer):
    class Meta:
        model = CassavaCheck
        fields = ('_all_')

class CassavaAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CassavaArea
        fields = ('__all__')