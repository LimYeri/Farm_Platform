from django.urls import path
from .views import *

urlpatterns = [
    path("livestream/", live, name = "livestream"),
    path("farmer_diary/", farmer_diary, name = "farmer_diary"),
   
]

