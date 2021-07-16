from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('policeofficerentry/', PoliceOfficerEntryView,
         name="Police Officer Entry View"),
    path('policeofficerhome/', PoliceOfficerHomeView,
         name="Police Officer Home View"),
    path('policeofficerupdate/<int:id>/', PoliceOfficerUpdateView,
         name='Police Officer Update View')
]
