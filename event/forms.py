from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import OrganizeEvent


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=15)
    last_name = forms.CharField(required=True, max_length=15)


    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email



class OrganizeEventForm(forms.ModelForm):
    class Meta:
        model = OrganizeEvent
        fields = [
            'event_name', 'event_date', 'event_description', 
            'your_name', 'your_email', 'your_phone', 
            'event_type', 'event_time', 'location', 'status'
        ]
        labels = {
            'event_name': 'Event Name',
            'event_date': 'Event Date',
            'event_description': 'Event Description(1000 Words)',
            'your_name': 'Your Name',
            'your_email': 'Your Email',
            'your_phone': 'Your Phone Number',
            'event_type': 'Type of Event',
            'event_time': 'Event Time',
            'location': 'Event Location',
            'status': 'Event Status',
        }
        help_texts = {
            'event_description': 'Provide a detailed description of the event.',
            'your_phone': 'Include your country code.',
        }
        widgets = {
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the event name'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'your_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'your_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'your_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'event_type': forms.Select(attrs={'class': 'form-control'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the event location'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        exclude = ['user']



