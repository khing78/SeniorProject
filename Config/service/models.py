from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class UidStore (models.Model) :
    email = models.EmailField(max_length=40)
    uId = models.CharField(max_length=30, primary_key=True)

class FarmStore (models.Model) :
    uidStore = models.ForeignKey(UidStore, on_delete=models.CASCADE)
    farmId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    farmName = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    plantingDate = models.DateField(default=timezone.now)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitudeMark1 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitudeMark1 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitudeMark2 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitudeMark2 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitudeMark3 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitudeMark3 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitudeMark4 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitudeMark4 = models.DecimalField(max_digits=30, decimal_places=15, default=0)

class Result (models.Model) :
    farmStore = models.ForeignKey(FarmStore, default=None, on_delete=models.CASCADE)
    starch_percentage = models.FloatField(max_length=6)
    checkDate = models.DateField(default=timezone.localdate)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)

class CassavaArea (models.Model) :
    farmStore = models.ForeignKey(FarmStore, default=None, on_delete=models.CASCADE)
    cassavaAreaId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    starchPercentage = models.FloatField(max_length=20)
    treeLatitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    treeLongtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    treewidth = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    treeLong = models.DecimalField(max_digits=30, decimal_places=15, default=0)

class CassavaCheck (models.Model) :
    cassavaArea = models.ForeignKey(CassavaArea, default=None, on_delete=models.CASCADE)
    checkDate = models.DateTimeField(auto_now_add=True, blank=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    spectrum1 = models.FloatField(max_length=20)
    spectrum2 = models.FloatField(max_length=20)
    spectrum3 = models.FloatField(max_length=20)
    spectrum4 = models.FloatField(max_length=20)
    semperature = models.FloatField(max_length=20)
    starchPercentage = models.FloatField(max_length=20)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)