from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, OrganizeEventForm
from django.contrib import messages
from .models import OrganizeEvent
from django.contrib.auth.decorators import login_required

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


def profile(request, id):
    data = get_object_or_404(User, pk=id)

    context = {
        'data':data
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