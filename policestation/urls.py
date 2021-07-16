from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('policestationentry/', PoliceStationEntryView,
         name="Police Staion Entry View"),
    path('policestationhome/', PoliceStationHomeView,
         name="Police Staion Home View"),
    path('policestationupdate/<int:id>/', PoliceStationUpdateView,
         name='Police Station Update View')
]
