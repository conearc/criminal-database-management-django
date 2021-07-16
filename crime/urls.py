from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [

    path('crimeentry/', CrimeEntryView, name="Crime Entry View"),
    path('crime/', CrimeView, name="Crime Home Page"),
    path('crimelist/', CrimeListView, name="Crime List View"),
    path('crimeupdate/<int:id>/', CrimeUpdateView,
         name='Crime Update View')

]
