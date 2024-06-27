from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, OrganizeEventForm
from django.contrib import messages
# Create your views here.

def home(request):
    
    return render(request, "home.html")


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
            return redirect('account')
        else:
            messages.error(request, "Wrong Username or Password!")
            return redirect('login')
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }

    return render(request, "login.html", context)


def profile(request, id):
    data = get_object_or_404(User, pk=id)

    context = {
        'data':data
        }    
    
    return render(request, "account.html", context)



def signoff(request):
    logout(request)
    return render (request, "home.html")



def organize_event(request):
    if request.method == 'POST':
        form = OrganizeEventForm(request.POST)

        if form.is_valid():
            form.save()
        
    else:
        form = OrganizeEventForm()

    context = {
        'form':form
        }
    return render(request, "organize.html", context)