from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, OrganizeEventForm
from django.contrib import messages
from .models import OrganizeEvent
from django.contrib.auth.decorators import login_required
import requests
import json
from datetime import datetime
from event_management.secrete import API_KEY
import asyncio


# Create your views here.

def home(request):
    url =  "http://worldtimeapi.org/api/timezone/Asia/Kathmandu"
    try:
        respose = requests.get(url)
        data = respose.json()
        date_data = data.get('datetime')
        time_zone = data.get('timezone')
    except Exception as e:
        return render(request, {'error':str(e)})
     
    if date_data:
        datetime_obj = datetime.fromisoformat(date_data.rstrip('Z'))
        formatted_date_time = datetime_obj.strftime('%Y-%m-%d %H:%M')
    else:
        formatted_date_time = None

    context = {
        'date_data':formatted_date_time,
        'time_zone':time_zone
    }
    return render(request, "home.html", context)



def registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)      

        if form.is_valid():
            email = form.cleaned_data['email']

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('signup')
            else:
                form.save()
                messages.success(request, "Registration Success. Please Login.")
                return redirect('login')
            
    return render(request, "signup.html", {'form':form})


def signin(request):    
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account', id=user.id)
        else:
            messages.error(request, "Wrong Username or Password!")
            return redirect('login')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }

    return render(request, "login.html", context)


@login_required
def profile(request, id):
    data = get_object_or_404(User, pk=id)
    my_data = OrganizeEvent.objects.filter(user=request.user)
    context = {
        'data':data,
        'my_event':my_data
        }    
    
    return render(request, "account.html", context)



def signoff(request):
    logout(request)
    return render (request, "home.html")


@login_required
def organize_event(request):
    if request.method == 'POST':
        form = OrganizeEventForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                if OrganizeEvent.objects.filter(user=request.user).count() < 5:
                    event = form.save(commit=False)
                    event.user = request.user
                    event.save()
                    messages.success(request, "Event organized successfully!")
                    return redirect('account')
                else:
                    messages.error(request, "You can only organize up to 5 events. Please Upgrade Your Account.")
            else:
                messages.error(request, "You must be logged in to organize an event.")
                return redirect('login')
    else:
        form = OrganizeEventForm()

    context = {
        'form': form
    }
    return render(request, "organize.html", context)



"""
   Get's data from weather API.
   Region specific only for Kathmandu
"""
def browse_events(request):
    all_events = OrganizeEvent.objects.order_by('-created_at')
    location = "kathmandu"
    url ="http://api.weatherapi.com/v1/current.json"

    params = {
        'key': API_KEY,
        'q': location
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        response.raise_for_status()
        data = response.json()
        date_data = data.get('location', {}).get('name', '')
        timezone = data.get('location', {}).get('localtime', '')
        current_temp = data.get('current', {}).get('temp_c', '')
        condition = data.get('current', {}).get('condition', {}).get('text', '')
        cond_icon = data.get('current', {}).get('condition', {}).get('icon', '')


    context = {
        'all_events':all_events,
        'date_data':date_data,
        'timezone':timezone,
        'current_temp':current_temp,
        'condition':condition,
        'cond_icon':cond_icon
    }
    return render(request, "all_event.html", context)



def browse_detail_event(request, id):
    detail_data = get_object_or_404(OrganizeEvent, pk=id)
    context = {
        'detail_data':detail_data
    }

    return render(request, "detail_event.html", context)


def volunteer(request):
    return render(request, "volunteer.html")


