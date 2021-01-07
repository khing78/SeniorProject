from django.contrib import admin
from .models import UidStore, FarmStore, Result, CassavaArea, CassavaCheck

# Register your models here.
admin.site.register(UidStore)
admin.site.register(FarmStore)
admin.site.register(Result)
admin.site.register(CassavaArea)
admin.site.register(CassavaCheck)

