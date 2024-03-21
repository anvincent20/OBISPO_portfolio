from django.urls import path
from . import views
app_name = 'base' 

urlpatterns = [
    path ('', views.home, name='home'),
    path ('cms/', views.cms, name='cms'),
    path ('introform/', views.personalprofile, name='introform'),
    
]