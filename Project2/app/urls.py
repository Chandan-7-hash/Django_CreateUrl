from django.urls import path
from app.views import *
urlpatterns = [
    path('',Home,name='Home'),
    path('home',Home,name='Home'),
    path('register',Register,name='reg'),
    path('login',Login,name='log'),
    
    
]
