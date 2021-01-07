from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = router.urls