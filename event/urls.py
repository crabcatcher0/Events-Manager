from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'), 
    path('organize/', organize, name='organize')
]

