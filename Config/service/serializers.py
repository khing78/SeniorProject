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
        fields = ('__all__')

class CassavaCheckSerializers(serializers.ModelSerializer):
    class Meta:
        model = CassavaCheck
        fields = ('__all__')
class CassavaAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CassavaArea
        fields = ('__all__')