from django.urls import path
from . import views
app_name = 'base' 

urlpatterns = [
    path ('', views.home, name='home'),
    path ('cms/', views.cms, name='cms'),

    #POST REQUEST ENDPOINTS
    path ('personalprofile/', views.personalprofile, name='personalprofile'),
    path ('aboutme/', views.aboutme, name='aboutme'),
    path ('project/', views.project, name='project'),
    path ('socialmedia/', views.socialmedia, name='socialmedia'),



    
]