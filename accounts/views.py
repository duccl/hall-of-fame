from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView,LogoutView

class SignUpView(CreateView):
    form_class = CustomUserCretionForm
    template_name = 'accounts/signup.html'
    def get_success_url(self):
        user = authenticate(self.request,username=self.request.POST.get('username'),password=self.request.POST.get('password1'))
        login(self.request,user=user)
        if self.request.user.is_authenticated:
            return reverse('halls:dashboard',kwargs={'user_id':user.pk})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('halls:home')