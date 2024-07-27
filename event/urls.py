from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'), 
    path('organize/', organize_event, name='organize'),
    path('signup/', registration, name='signup'),
    path('login/', signin, name='login'),
    path('account/<int:id>/', profile, name='account'),
    path('logout/', signoff, name='logout'),
    path('all_events/', browse_events, name='all_events'),
    path('detail_events/<int:id>/', browse_detail_event, name='detail_events'),

]

