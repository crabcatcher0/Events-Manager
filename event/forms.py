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
        fields = '__all__'