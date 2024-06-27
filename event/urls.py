from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'), 
    path('organize/', organize_event, name='organize'),
    path('signup/', registration, name='signup'),
    path('login/', signin, name='login'),
    path('account/<int:id>/', profile, name='account'),
    path('logout/', signoff, name='logout'),
]

