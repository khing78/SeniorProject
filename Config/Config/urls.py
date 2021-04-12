"""Config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('uids/', views.uid_collected, name="uid-get&crate"),
    path('uids/<str:pk>/', views.uid_editor, name="uid-edit"),
    path('farms/', views.farm_list, name="farmlist-get&post"),
    path('farms/<str:pk>/', views.farm_detail, name="farmlist-PUT&DELETE"),
    path('result/', views.result, name="show-result"),
    path('cassava-check/', views.cassava_check, name="cassava-check"),
    path('cassava-check/<str:pk>/', views.cassava_check_editor, name="cassava-check"),
    path('area-check/', views.area_check_get, name="area-check"),
    path('area-check/<str:pk>/', views.area_check, name="area-check-update-delete"),
    path('cassava_test/<str:uid_store>/', views.cassava_check_farm, name="cassava_check_farm"),
    path('area_check_create/<str:uid_store>/', views.area_check_create, name="for create area")
]
