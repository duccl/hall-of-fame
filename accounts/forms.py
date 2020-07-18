from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCretionForm(UserCreationForm):
    profile_pic = forms.ImageField()
    about = forms.CharField()

    class Meta():
        model = User
