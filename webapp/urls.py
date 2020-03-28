from django.conf.urls import url
from django.urls import path, include
from django.conf.urls import url
from webapp.views import *
from rest_framework import routers


urlpatterns = [
    path('', Home),
    path('profile/',profile),
    path('home/',HomeView),
    path('logout/', LogOut),


]
