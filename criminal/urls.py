from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('criminalentry/', CriminalEntryView, name="Criminal Entry View"),
    path('criminal/', CriminalView, name="Criminal Home Page"),
    path('searchcriminal', SearchCriminal, name="Search Criminal View"),
    path('deletecriminal/<int:id>/', DeleteCriminal, name="Delete Criminal"),
    path('criminalupdate/<int:id>/', CriminalUpdateView,
         name='Criminal Update View')
]
