from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'), 
    path('organize/', organize, name='organize'),
    path('signup/', registration, name='signup'),
    path('login/', signin, name='login'),
    path('account/', profile, name='account'),
]

