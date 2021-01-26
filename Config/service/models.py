from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class UidStore (models.Model) :
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    uId = models.CharField(max_length=30, primary_key=True)

class FarmStore (models.Model) :
    uid_store = models.ForeignKey(UidStore, on_delete=models.CASCADE)
    farm_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    farm_name = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    planting_date = models.DateField(default=timezone.now)
    farm_width = models.FloatField(max_length=6)
    farm_long = models.FloatField(max_length=6)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitude_mark1 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude_mark1 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitude_mark2 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude_mark2 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitude_mark3 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude_mark3 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    latitude_mark4 = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude_mark4 = models.DecimalField(max_digits=30, decimal_places=15, default=0)

class Result (models.Model) :
    farm_store = models.ForeignKey(FarmStore, default=None, on_delete=models.CASCADE)
    starch_percentage = models.FloatField(max_length=6)
    check_date = models.DateField(default=timezone.localdate)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)

class CassavaArea (models.Model) :
    farm_store = models.ForeignKey(FarmStore, default=None, on_delete=models.CASCADE)
    cassava_area_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    starch_percentage = models.FloatField(max_length=20, null=True, blank=True, default=None)
    tree_latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    tree_longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)

class CassavaCheck (models.Model) :
    cassava_area = models.ForeignKey(CassavaArea, default=None, on_delete=models.CASCADE)
    check_date = models.DateTimeField(auto_now_add=True, blank=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    longtitude = models.DecimalField(max_digits=30, decimal_places=15, default=0)
    spectrum1 = models.FloatField(max_length=20)
    spectrum2 = models.FloatField(max_length=20)
    spectrum3 = models.FloatField(max_length=20)
    spectrum4 = models.FloatField(max_length=20)
    spectrum5 = models.FloatField(max_length=20)
    spectrum6 = models.FloatField(max_length=20)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    humidity = models.DecimalField(max_digits=10, decimal_places=2)
    starchPercentage = models.FloatField(max_length=20)