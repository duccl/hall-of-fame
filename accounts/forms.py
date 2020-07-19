from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCretionForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)
    about = forms.CharField(required=False)

    def save(self, commit=True):
        user = super(CustomUserCretionForm,self).save()
        user_profile = UserProfile(user=user,image=self.cleaned_data['profile_pic'])
        print(user_profile.image,self.cleaned_data['profile_pic'],self.cleaned_data)
        if self.cleaned_data.get('about'):
            user_profile.about = self.cleaned_data.get('about')
        user_profile.save()
        return user,user_profile
