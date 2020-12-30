from django.db import models
from django.utils import timezone

# Create your models here.
class UidStore (models.Model) :
    email = models.EmailField(max_length=40)
    uId = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self

class FarmStore (models.Model) :
    uidStore = models.ForeignKey(UidStore, on_delete=models.CASCADE)
    farmName = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    plantingDate = models.DateField(default=timezone.now)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)

class Result (models.Model) :
    farmStore = models.ForeignKey(FarmStore, default=None, on_delete=models.CASCADE)
    grade = models.CharField(max_length=1)
    starch_percentage = models.FloatField(max_length=6)
    checkDate = models.DateField(default=timezone.localdate)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)

class CassavaCheck (models.Model) :
    farmStore = models.ForeignKey(FarmStore, default=None, on_delete=models.CASCADE)
    checkDate = models.DateTimeField(default=timezone.localdate)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    spectrum1 = models.FloatField(max_length=20)
    spectrum2 = models.FloatField(max_length=20)
    spectrum3 = models.FloatField(max_length=20)
    spectrum4 = models.FloatField(max_length=20)
    semperature = models.FloatField(max_length=20)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)