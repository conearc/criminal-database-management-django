from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('home/', HomePageView, name="home"),
    path('', LoginHomePageView, name="homepage"),
    path('login/', login2, name="loginhome"),
    path('register/', RegisterView),
    path("logout", logout_request, name="logout"),
]
