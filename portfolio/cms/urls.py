from django.urls import path
from .views import *

app_name = "cms"

urlpatterns = [
    path('login/', signin, name="signin"),
]